# Verification scope

## Written and finite evidence

The universal classification is a mathematical argument in the manuscript, not a computational enumeration. Appendix A supplies a finite exact-rational certificate for the distinct order-13 witness. The checker verifies coefficients through degree 23, parity, positive-time and tail inequalities, an analytic-transfer integer comparison and the final heat-conversion margin. The holomorphic, convolution, Fourier and Cauchy arguments remain written proofs.

The original assertion-based listing was replaced by explicit named guards. No old assertion-disabled logs are used as evidence for the repaired implementation. The repair transcribes the original formulas; it is not an independently designed second mathematical implementation.

## Commands

From the repository directory, use new output filenames each time:

```sh
python3 -B checks/tsallis_order13_certificate.py --output /tmp/tsallis-positive-UNIQUE.json
python3 -B checks/test_guards.py --output /tmp/tsallis-negative-UNIQUE.json
python3 -B -O checks/tsallis_order13_certificate.py --output /tmp/tsallis-positive-opt-UNIQUE.json
python3 -B -O checks/test_guards.py --output /tmp/tsallis-negative-opt-UNIQUE.json
```

Replace UNIQUE with a fresh run identifier. Existing output paths are rejected, never overwritten. Python 3.14.7 with standard library only was observed for the repaired-source replay on 6 November 2026.

Both positive receipts were byte-identical, SHA256 `37e6c66d4fba19b5cf405baf34f52988e6e707d580216e3b342741769d5b34dd`.
All eleven corruptions failed at their intended guards in both modes: POSITIVITY, ANALYTIC_RADIUS, MODULUS_BOUND, PARITY, TAIL_RATIO, ZERO_TIME_SIGN, FINITE_SUM, TAIL_BOUND, POSITIVE_TIME_SIGN, CAUCHY_ERROR, ENTROPY_MARGIN.
The normal negative receipt SHA256 was `74d1f313c17cb99e774973e594b27363eeae3e8805d7a22a4dc91348b147a7e5`; optimized negative was `fc4d61bac1e2c23bdc9c2cdb5257baf0c3e056b0b85adf8b0b264b4c43d856a0`.

An AST check found no Assert nodes in the shipped checker modules. A separate overwrite test preserved the existing receipt. These are implementation checks, not a proof of the theorem.

## Manuscript and release boundary

The 17-page PDF was compiled with pdfLaTeX and inspected visually, including the scope table and all mathematical displays. Final archive extraction, manifest verification, metadata and provider parity are separate gates: the working-source replay is not silently relabelled a frozen-archive replay. No formal proof or external independent reproduction is claimed.
