# RK3588 Vision Deployment — Free Sample

One model, end to end, measured on real RK3588 hardware: MobileNetV2
(FP + INT8 artifacts included), a runnable classification example, and the
summary leaderboard of everything we measured (14 models, 25 configurations:
latency p50/p95, per-op CPU fallback, memory).

Verified stack: rknn-toolkit2 2.3.2 / librknnrt 2.3.2 / driver 0.9.8,
Ubuntu 22.04, kernel 6.1.118.

## Run it
See `example_classify_mobilenetv2/README.md`. On our board the example's
top-1 for the bundled test image is zebra, 0.9993 — for both the FP and the
INT8 artifact.

## The full kit
This sample is one model out of the **RK3588 Vision Deployment Starter Kit**:

- config-driven ONNX→RKNN pipeline (FP + INT8 + hybrid quantization recipes)
- board benchmark runner + per-op CPU fallback analyzer
- 12 verified artifacts, 6 models (classification, detection, OCR, face)
- full raw measurement reports, complete fallback tables, and the
  failure-path archive — including a documented toolkit 2.3.2 bug that
  inflates one INT8 artifact to 18 MB of zero padding, and what we did
  about it
- 5 runnable examples, version matrix, licenses with full provenance

Starter $79 / Complete $149 on Gumroad (search "RK3588 Vision Deployment
Starter Kit" at edgemodellab.gumroad.com). We don't sell models — the
models are free. The kit sells the two weeks of setup and dead ends you
don't have to repeat.

## License of this sample
Example code: MIT. Model artifacts: Apache-2.0 (ONNX Model Zoo /
MobileNetV2). Leaderboard data: cite with attribution.
