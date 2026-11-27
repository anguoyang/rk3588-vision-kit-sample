# Quickstart (free sample)

The free sample contains one complete, runnable slice of the kit:
MobileNetV2 classification, FP and INT8, end to end. It exists so you can
verify the pipeline, the documentation style, and the data format before
spending anything.

## 1. Get the runtime in place

The kit does not redistribute Rockchip's proprietary runtime. Install
`librknnrt` 2.3.2 using the vendor package for your board, then verify:

```bash
strings /usr/lib/librknnrt.so | grep -i "librknnrt version"
# expected: librknnrt version: 2.3.2
```

Only the combinations in the [Version Matrix](version-matrix.md) are tested.

## 2. Run the sample

```bash
git clone https://github.com/anguoyang/rk3588-vision-kit-sample
cd rk3588-vision-kit-sample/example_classify_mobilenetv2
python3 run_classify.py --model ../models/mobilenetv2_rk3588_fp.rknn --image zebra.jpg
python3 run_classify.py --model ../models/mobilenetv2_rk3588_int8.rknn --image zebra.jpg
```

Expected output (measured on the reference board):

```
top-1: zebra  0.9993   (FP)
top-1: zebra  0.9993   (INT8)
```

## 3. Check the numbers

Compare your board against the reference measurements in
[Benchmarks](benchmarks.md). On the reference configuration, MobileNetV2
measures **8.63 ms p50 (FP)** and **4.15 ms p50 (INT8)**. A first-run result
~15% slower than that is a known platform effect, not a fault — see
[Known Issues](known-issues.md#first-context-effect).

## Next steps

- The full kit adds 11 more artifacts, detection/face/OCR examples, the
  conversion pipeline for your own models, and the complete raw reports.
- Questions: [FAQ](faq.md).
