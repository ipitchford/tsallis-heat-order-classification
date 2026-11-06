from guards import require, write_receipt
"""Exact periodic Tsallis alpha=3/2 sign certificate at derivative order 13.

For v(t,x)=1+(1/10)e^-t cos(x)+(1/32000)e^-4t cos(2x),
certify (-1)^13 d_t^13 mean(v(t,x)^(3/2))|t=1/100 < -6.
All explicit guards and the Cauchy tail bound use exact rational arithmetic.
The final integer comparison supports the separately proved analytic
transfer to a real-line probability density of Gaussian variance 2^40.
Adapted from research/low_order_trial/certificate_n13.py.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json
alpha = Q(3, 2)
a = Q(1, 10)
b = Q(1, 32000)
n = 13
radius = Q(8)
maximum_modulus = Q(3)
tail_start = 24

def binomial(q, degree):
    result = Q(1)
    for h in range(degree):
        result *= (q - h) / (h + 1)
    return result

def trig_mean(i, j):
    if i % 2:
        return Q(0)
    total = sum((comb(i, i // 2 + j - 2 * s) * comb(j, s) for s in range(j + 1) if 0 <= i // 2 + j - 2 * s <= i))
    return Q(total, 2 ** (i + j))

def coefficient(k):
    total = Q(0)
    for j in range(k // 4 + 1):
        i = k - 4 * j
        total += binomial(alpha, i + j) * comb(i + j, i) * a ** i * b ** j * trig_mean(i, j)
    return total

def main():
    require(a + b < 1, 'POSITIVITY')
    perturbation = a * radius + b * radius ** 4
    require(perturbation < 1, 'ANALYTIC_RADIUS')
    require((1 + perturbation) ** 3 < maximum_modulus ** 2, 'MODULUS_BOUND')
    coefficients = {k: coefficient(k) for k in range(tail_start)}
    require(all((coefficients[k] == 0 for k in range(1, tail_start, 2))), 'PARITY')
    partial = sum((coefficients[k] * k ** n for k in range(1, tail_start)))
    rho = Q(tail_start + 2, tail_start) ** n / radius ** 2
    require(rho < 1, 'TAIL_RATIO')
    tail = maximum_modulus * Q(tail_start) ** n / radius ** tail_start / (1 - rho)
    upper = partial + tail
    require(upper < -7, 'ZERO_TIME_SIGN')
    time = Q(1, 100)
    degree = 12
    exponential_lower = sum((time ** j / factorial(j) for j in range(degree + 1)))
    first_omitted = time ** (degree + 1) / factorial(degree + 1)
    exponential_upper = exponential_lower + first_omitted / (1 - time / (degree + 2))
    positive_time_partial_upper = sum((value * k ** n / (exponential_lower if value >= 0 else exponential_upper) ** k for k, value in coefficients.items() if k > 0))
    positive_time_upper = positive_time_partial_upper + tail
    require(positive_time_partial_upper < -Q(27, 4), 'FINITE_SUM')
    require(tail < Q(1, 1000), 'TAIL_BOUND')
    require(positive_time_upper < -6, 'POSITIVE_TIME_SIGN')
    gaussian_variance = 2 ** 40
    cauchy_error = Q(100 * factorial(n), gaussian_variance)
    require(cauchy_error < 1, 'CAUCHY_ERROR')
    entropy_margin = Q(2 * (6 - 1), 2 ** n)
    require(entropy_margin > Q(1, 1024), 'ENTROPY_MARGIN')
    record = {'status': 'PASS_EXACT_RATIONAL', 'scope': 'Exact finite arithmetic; real-line transfer requires the analytic lemma', 'heat_convention': 'partial_t v=partial_xx v', 'alpha': str(alpha), 'a': str(a), 'b': str(b), 'derivative_order': n, 'time': str(time), 'quantity': '(-1)^13 d_t^13 mean(v(t,x)^(3/2)) at t=1/100', 'radius': str(radius), 'maximum_modulus_bound': str(maximum_modulus), 'perturbation_on_radius': str(perturbation), 'tail_start': tail_start, 'coefficients': {str(k): str(value) for k, value in coefficients.items()}, 'zero_time_partial_sum': str(partial), 'tail_ratio': str(rho), 'tail_bound': str(tail), 'zero_time_signed_derivative_upper': str(upper), 'diagnostics': {'zero_time_partial_sum': float(partial), 'tail_bound': float(tail), 'zero_time_signed_derivative_upper': float(upper)}, 'positive_time_certificate': {'time': str(time), 'exponential_taylor_degree': degree, 'exponential_lower': str(exponential_lower), 'exponential_upper': str(exponential_upper), 'signed_derivative_upper': str(positive_time_upper), 'signed_derivative_upper_diagnostic': float(positive_time_upper), 'simple_partial_upper': '-27/4', 'simple_tail_upper': '1/1000', 'simple_total_upper': '-6749/1000', 'rigorous_conclusion': '(-1)^13 F^(13)(1/100) < -6'}, 'real_line_transfer': {'gaussian_variance': '2^40', 'cauchy_radius': '1', 'uniform_analytic_error_bound': '100/R', 'cauchy_error_upper': str(cauchy_error), 'cauchy_error_upper_diagnostic': float(cauchy_error), 'source_heat_convention': 'partial_t p = (1/2) partial_xx p', 'source_time': '1/50', 'conclusion': 'S_(3/2)^(13)(1/50) < -C_R/1024, conditional on the analytic transfer lemma'}, 'external_dependencies': []}
    write_receipt(record)
    summary = {k: v for k, v in record.items() if k not in ('coefficients', 'zero_time_partial_sum', 'tail_ratio', 'tail_bound', 'zero_time_signed_derivative_upper', 'positive_time_certificate')}
    summary['positive_time_certificate'] = {k: v for k, v in record['positive_time_certificate'].items() if k not in ('exponential_lower', 'exponential_upper', 'signed_derivative_upper')}
    print(json.dumps(summary, indent=2))
if __name__ == '__main__':
    main()
