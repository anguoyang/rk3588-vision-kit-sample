# Example 01 — Image classification (MobileNetV2)

End-to-end: load the kit's MobileNetV2 `.rknn`, run one image on the
RK3588 NPU, print ImageNet top-5.

## Environment

- RK3588 board, librknnrt 2.3.2 (matches the kit version matrix)
- Python 3 with `rknn-toolkit-lite2`, `numpy`, `opencv-python`
- Run from this directory on the board; the default model path is
  `../../models/mobilenetv2_rk3588_fp.rknn` (kit layout). The INT8
  model (`mobilenetv2_rk3588_int8.rknn`) works with the same script.

## Files

- `classify.py` — the whole example (preprocess → inference → top-5)
- `synset.txt` — 1000 ImageNet class labels (from the RKNN Model Zoo
  mobilenet example, Apache-2.0; see "Source & license" below)
- `test_zebra.jpg` — test photo (COCO val2017 image 000000215245)

## Run

```sh
python3 classify.py
# or explicitly:
python3 classify.py ../../models/mobilenetv2_rk3588_int8.rknn test_zebra.jpg
```

## Expected output

A `-----TOP 5-----` block whose top-1 is **zebra** for the bundled
test photo. (Exact scores are recorded in the kit verification log
after a board run.)

## Key point

No float preprocessing on the board: the model's normalization
(ImageNet mean/std in 255-space) was baked in at conversion time, so
the input is a raw uint8 RGB 224×224 image. Every example in this kit
follows that pattern.

## Source & license

Written for this kit against the `rknnlite` API. Model and labels come
from the RKNN Model Zoo mobilenet example
(https://github.com/airockchip/rknn_model_zoo, Apache-2.0); the model
itself is MobileNetV2 from the ONNX Model Zoo (Apache-2.0).

## Board verification (2026-11-27, rk2 / RK3588)

Verified on real hardware: librknnrt 2.3.2, driver 0.9.8,
rknn-toolkit-lite2 2.3.2 (board loadavg ≈17 during the run; this
example is a single inference, timing is not the claim here).

FP model (`mobilenetv2_rk3588_fp.rknn`), bundled `test_zebra.jpg`:

```
-----TOP 5-----
[340] score=0.9993 class="n02391049 zebra"
[912] score=0.0005 class="n04604644 worm fence, snake fence, snake-rail fence, Virginia fence"
[351] score=0.0000 class="n02422106 hartebeest"
[352] score=0.0000 class="n02422699 impala, Aepyceros melampus"
[730] score=0.0000 class="n03967562 plow, plough"
```

INT8 model (`mobilenetv2_rk3588_int8.rknn`), same image: top-1 is
again `[340] zebra` at 0.9993 (remaining top-5 order differs slightly:
gazelle appears at rank 3). Both precisions pass.
