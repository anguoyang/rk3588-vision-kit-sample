# RK3588 Vision Deployment Kit

**Skip the two-week setup.** This kit is a verified ONNX → RKNN deployment
pipeline for the Rockchip RK3588: converted model artifacts, a tested version
matrix, per-operator CPU-fallback data, and measurements taken on real
hardware — not on an emulator, not copied from a datasheet.

This documentation is **free and complete**. Read everything, check the
numbers, run the free sample. The paid package contains the runnable
artifacts, the full raw measurement data, and the tuned conversion scripts.

## What you get

| | Free (this site + sample repo) | Starter ($79) | Complete ($149) |
|---|---|---|---|
| Full documentation (methods, matrix, results, failure records) | ✅ | ✅ | ✅ |
| MobileNetV2 end-to-end sample (FP + INT8 artifacts) | ✅ | ✅ | ✅ |
| Conversion pipeline (all models) | — | ✅ | ✅ |
| 12 converted artifacts (FP + INT8) | — | ✅ | ✅ |
| Worked examples (classify, detect, face) | — | ✅ | ✅ |
| OCR + bring-your-own-model examples | — | — | ✅ |
| Full raw measurement reports (25 files) | — | — | ✅ |
| Conversion notes & calibration details | — | — | ✅ |
| Updates | — | 6 months | 12 months |

## Measured environment

All numbers on this site were measured on one documented configuration:

- **SoC / board:** Rockchip RK3588
- **OS:** Ubuntu 22.04.5 LTS, kernel 6.1.118
- **Runtime:** librknnrt 2.3.2 · **Driver:** rknpu 0.9.8
- **Conversion:** rknn-toolkit2 2.3.2 (x86_64 host)

See the [Version Matrix](version-matrix.md) for the exact tested
combinations, and [Benchmarks](benchmarks.md) for the measurement protocol.
Numbers measured outside this matrix are marked as such wherever they appear.

## Why not just do it yourself?

You can. The official guides are free. What they don't give you:

- **Artifacts that are already verified on hardware**, with SHA-256 hashes.
- **The failure records** — which INT8 calibration silently collapses a
  detector's confidence scores, which artifact balloons to 18 MB because of a
  compiler memory-planning quirk, which ops fall back to CPU and by how much.
  See [Known Issues](known-issues.md).
- **A version matrix that is known to work as a set**, instead of three days
  of toolkit/driver/runtime mismatch debugging.

That is what the package sells: the two weeks, already spent.

## Get the kit

- Starter — $79 · Complete — $149, via Gumroad (EdgeModelLab store)
- Free sample: the GitHub repository linked above (MobileNetV2, full pipeline)
- Support: see [FAQ](faq.md). 14-day refund if the pipeline does not run as
  documented on a version-matrix configuration.

```{toctree}
:hidden:
:maxdepth: 2

quickstart
version-matrix
benchmarks
known-issues
faq
```
