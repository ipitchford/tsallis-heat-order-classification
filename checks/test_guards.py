"""Semantic corruptions must fail at the intended optimization-safe guard."""
import ast
import contextlib
import io
import json
import sys
from decimal import localcontext
from pathlib import Path
from guards import VerificationError, require, write_receipt

HERE = Path(__file__).resolve().parent

class InsertCorruption(ast.NodeTransformer):
    def __init__(self, code, assignment):
        self.code, self.assignment, self.count = code, assignment, 0
    def visit_Expr(self, node):
        call = node.value
        if (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                and call.func.id == 'require' and len(call.args) >= 2
                and isinstance(call.args[1], ast.Constant)
                and call.args[1].value == self.code):
            self.count += 1
            return ast.parse(self.assignment).body + [node]
        return self.generic_visit(node)

def check_case(filename, code, assignment, entry):
    path = HERE / filename
    tree = ast.parse(path.read_text())
    require(not any(isinstance(n, ast.Assert) for n in ast.walk(tree)), 'NO_REMOVABLE_ASSERTS')
    if assignment is not None:
        change = InsertCorruption(code, assignment)
        tree = change.visit(tree)
        require(change.count == 1, 'UNIQUE_GUARD_TARGET')
    ast.fix_missing_locations(tree)
    env = {'__name__': 'semantic_test', '__file__': str(path)}
    exec(compile(tree, str(path), 'exec', optimize=sys.flags.optimize), env)
    # Any attempted receipt is itself a failure; invalid executions cannot emit success.
    env['write_receipt'] = lambda record: require(False, 'INVALID_CASE_REACHED_RECEIPT')
    try:
        with contextlib.redirect_stdout(io.StringIO()), localcontext() as ctx:
            ctx.prec = 160
            eval(entry, env)
    except VerificationError as exc:
        require(exc.code == code, 'WRONG_GUARD_' + exc.code)
        return {'guard': code, 'outcome': 'rejected_at_intended_guard'}
    raise RuntimeError('INVALID_CASE_ACCEPTED_' + code)

def main():
    records = [check_case(*case) for case in CASES]
    record = {'status': 'PASS_SEMANTIC_NEGATIVES', 'optimization': sys.flags.optimize,
              'cases': records, 'count': len(records),
              'scope': 'Guard sensitivity only; not a proof of universal mathematics'}
    write_receipt(record)
    print(json.dumps(record, indent=2))

CASES = [
  [
    "tsallis_order13_certificate.py",
    "POSITIVITY",
    "a = Q(1)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "ANALYTIC_RADIUS",
    "perturbation = Q(2)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "MODULUS_BOUND",
    "maximum_modulus = Q(1)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "PARITY",
    "coefficients[1] = Q(1)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "TAIL_RATIO",
    "rho = Q(2)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "ZERO_TIME_SIGN",
    "upper = Q(0)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "FINITE_SUM",
    "positive_time_partial_upper = Q(0)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "TAIL_BOUND",
    "tail = Q(1)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "POSITIVE_TIME_SIGN",
    "positive_time_upper = Q(0)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "CAUCHY_ERROR",
    "cauchy_error = Q(1)",
    "main()"
  ],
  [
    "tsallis_order13_certificate.py",
    "ENTROPY_MARGIN",
    "entropy_margin = Q(0)",
    "main()"
  ]
]

if __name__ == '__main__':
    main()

