# Agent reading index

## Identity and status
Title: Complete monotonicity of Tsallis entropy under heat flow: a sharp order classification.
Version: 0.1.0-candidate. Creator: Anonymous. Date: 6 November 2026.
Version DOI: 10.5281/zenodo.24001602. A DOI identifier alone is not evidence of public availability.
AI-assisted unrefereed candidate; no external human review, independent reproduction or proof-assistant verification is claimed.

## Claims and proof locations
- Universal positive-order classification: [paper.md](paper.md) Theorem 1; assembled from Theorem 2, inherited Shannon failure and the quadratic Fourier argument.
- Nonexceptional Tsallis orders: Theorem 2, Lemmas 3–4 and subsequent proof. Density depends on the derivative order; the proof is pointwise in the entropy parameter.
- Quadratic positivity: Section 4, inherited/source-attributed identity.
- Explicit finite witness: Theorem 7 and Appendix A. Order 3/2, derivative 13, heat time 1/50. No log-concavity or optimal-order assertion.
- Elementary dilation: Corollary 8. Positive rescaling preserves the derivative sign; variance and time cannot both be assigned freely.

## Evidence and execution
Written proofs are in [paper.md](paper.md) and [paper.tex](paper.tex); [paper.pdf](paper.pdf) is the typeset rendition.
[checks/tsallis_order13_certificate.py](checks/tsallis_order13_certificate.py) verifies finite rational inequalities.
[checks/test_guards.py](checks/test_guards.py) tests eleven intended failures in normal and optimized Python.
[checks/guards.py](checks/guards.py) supplies explicit guards and exclusive receipt creation.
[VERIFICATION.md](VERIFICATION.md) gives commands, evidence hashes and exact boundaries. Execution is not proof adequacy.

## Dependencies and prior art
[refs.bib](refs.bib) is the machine-readable bibliography. [SOURCES.md](SOURCES.md) and [CITATION_AUDIT.md](CITATION_AUDIT.md) map pinned source versions to inherited facts and the bounded novelty comparison. The periodic/Gaussian method is not claimed new. Search absence is not priority proof.

## Objections, provenance and limits
[RESPONSE_TO_REVIEW.md](RESPONSE_TO_REVIEW.md) records substantive revisions without private evaluations.
[LIMITATIONS.md](LIMITATIONS.md) records quantifier, computational and priority limits.
[PROVENANCE.md](PROVENANCE.md) distinguishes original inputs, revised sources and repaired replay.
[RESEARCH_GATES.json](RESEARCH_GATES.json) records contribution and limitation triage. Final archive integrity and provider availability are separate release operations.

## Licence
[LICENSES.md](LICENSES.md) maps original prose/data to CC0-1.0 and original code to MIT. Third-party works are cited, not relicensed.
