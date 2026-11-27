# Benchmarks

## Protocol

Every number below was produced the same way, on the
[reference configuration](version-matrix.md):

- **Warmup:** 10 runs, then **50 timed runs** per session
- **Sessions:** 3 independent sessions, each in its own process;
  the reported value is the **median of session medians**
- **Priming:** one sacrificial load + 5-run cycle in a separate process
  before measuring (see the
  [first-context effect](known-issues.md#first-context-effect))
- **Timer:** NPU `PERF_RUN` profiling; CPU-fallback share computed from
  per-operator timings
- **Verdict:** `NPU_ONLY` = no operator executed on CPU;
  `MIXED` = some operators fell back (share shown)

Single-session numbers on this SoC can sit ~15% off the sustained state;
that is why the protocol above is not optional when comparing.

## Results (23 measured configurations, 14 models)

| Model | Task | Precision | p50 (ms) | p95 (ms) | FPS (p50) | Verdict | CPU fallback |
|---|---|---|---|---|---|---|---|
| MobileNetV2 | classify | FP | 8.63 | 8.89 | 115.9 | NPU_ONLY | 0% |
| MobileNetV2 | classify | INT8 | 4.15 | 4.65 | 241.3 | MIXED | 1.10% |
| ResNet50-v2 | classify | FP | 25.40 | 29.34 | 39.4 | NPU_ONLY | 0% |
| ResNet50-v2 | classify | INT8 | 13.54 | 15.26 | 73.8 | MIXED | 0.63% |
| RetinaFace (Mobile320) | face-detect | FP | 6.43 | 6.68 | 155.6 | MIXED | 4.05% |
| RetinaFace (Mobile320) | face-detect | INT8 | 7.99 | 8.35 | 125.2 | MIXED | 2.74% |
| YOLO11n | detect | FP | 43.67 | 49.79 | 22.9 | NPU_ONLY | 0% |
| YOLO11n | detect | INT8 | 31.20 | 31.69 | 32.1 | NPU_ONLY | 0% |
| YOLOv5s (ReLU) | detect | FP | 37.81 | 38.58 | 26.5 | NPU_ONLY | 0% |
| YOLOv5s (ReLU) | detect | INT8 | 20.52 | 22.30 | 48.7 | NPU_ONLY | 0% |
| YOLOv8n | detect | FP | 37.50 | 38.58 | 26.7 | NPU_ONLY | 0% |
| YOLOv8n | detect | INT8 | 19.17 | 19.76 | 52.2 | NPU_ONLY | 0% |
| YOLOv10s | detect | FP | 88.09 | 90.49 | 11.4 | NPU_ONLY | 0% |
| YOLOv8n-obb | detect-obb | FP | 37.65 | 38.26 | 26.6 | NPU_ONLY | 0% |
| YOLOv8n-pose | pose | FP | 49.74 | 51.27 | 20.1 | NPU_ONLY | 0% |
| YOLOv8n-pose | pose | INT8 | 31.64 | 32.71 | 31.6 | NPU_ONLY | 0% |
| YOLOv8n-seg | segment | FP | 46.74 | 57.36 | 21.4 | NPU_ONLY | 0% |
| YOLOv8s-seg | segment | FP | 104.54 | 113.09 | 9.6 | NPU_ONLY | 0% |
| YOLOv8s-seg | segment | INT8 | 43.84 | 45.44 | 22.8 | NPU_ONLY | 0% |
| PP-YOLOE-s | detect | FP | 67.71 | 70.44 | 14.8 | NPU_ONLY | 0% |
| PP-YOLOE-s | detect | INT8 | 35.80 | 36.42 | 27.9 | NPU_ONLY | 0% |
| PP-OCRv4-Det | ocr-detect | FP | 47.86 | 49.99 | 20.9 | NPU_ONLY | 0% |
| PP-OCRv4-Det | ocr-detect | INT8 | 31.39 | 39.99 | 31.9 | NPU_ONLY | 0% |
| PP-OCRv4-Rec | ocr-recognize | FP | 22.68 | 26.45 | 44.1 | MIXED | 2.58% |
| PP-OCRv4-Rec | ocr-recognize | INT8 | 14.16 | 16.96 | 70.6 | MIXED | 2.61% |

## How to read this table

- **INT8 is not automatically faster.** RetinaFace INT8 is *slower* than its
  FP build on this stack and is shipped as a measurement record; the FP
  artifact is the recommended one. Details in
  [Known Issues](known-issues.md#retinaface-int8).
- **MIXED is not broken.** A few `Reshape` operators routinely fall back to
  CPU with a small time share. What matters is the share, which is printed
  for every model — most vendor tables omit it.
- **Full raw reports** (per-operator timings, memory deltas, session-level
  data) are in the Complete package. The summary above is complete and free;
  the raw files are what you re-check a procurement decision against.
