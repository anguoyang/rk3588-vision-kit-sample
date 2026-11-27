# FAQ

## Buying

**What exactly am I paying for, if the documentation is free?**
The runnable artifacts (12 converted models, FP + INT8), the conversion
pipeline scripts, the worked examples, and — in Complete — the full raw
measurement reports and conversion notes. The documentation is free because
it is how you verify the package is real before paying.

**Is there a free trial?**
The free sample (GitHub) is one complete model end to end — pipeline,
artifacts, and data format identical to the paid kit. Together with this
documentation, that is the trial. There is no time-locked demo; code does
not work that way.

**Refund policy**
14 days: if the pipeline does not run as documented on a configuration
inside the [Version Matrix](version-matrix.md), after working through the
self-check list and support, you get a full refund.

## Technical

**Can I use the artifacts in a commercial product?**
Yes. The kit license covers commercial use of the pipeline, examples, and
data. Model weights keep their upstream licenses — each artifact's origin
and license is listed in `LICENSES.md` inside the package. Only weights with
redistribution-compatible licenses (Apache / MIT / BSD) are included.

**Why is `librknnrt` not in the package?**
It is Rockchip-proprietary and not ours to redistribute. The package ships
sideload instructions and a version check instead.

**My numbers differ from the Benchmarks page.**
First check the [first-context effect](known-issues.md#first-context-effect)
and whether your versions match the matrix. Then compare per-session: the
protocol (3 sessions, median) matters more than any single run.

**Does INT8 always help?**
No — see RetinaFace in [Known Issues](known-issues.md#retinaface-int8). The
kit tells you per model instead of assuming.

## Support

- Scope: configurations inside the version matrix, after the self-check list
  in the package `README.md`.
- Contact: the support address printed in the package.
- Updates: new package versions are posted to the Gumroad library; download
  the new version from your library page. Starter includes 6 months of
  updates, Complete 12 months.
