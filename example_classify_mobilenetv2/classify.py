#!/usr/bin/env python3
"""MobileNetV2 image classification on RK3588 (rknn-toolkit-lite2).

The kit's mobilenetv2_rk3588_*.rknn models were converted with the
ImageNet normalization (mean 255*[0.485,0.456,0.406],
std 255*[0.229,0.224,0.225]) baked into the model, so the board-side
input is a plain uint8 RGB image resized to 224x224 -- no float
preprocessing needed.

Usage:
    python3 classify.py [model.rknn] [image.jpg]
Defaults: ../../models/mobilenetv2_rk3588_fp.rknn, ./test_zebra.jpg
"""
import sys

import cv2
import numpy as np
from rknnlite.api import RKNNLite

MODEL = sys.argv[1] if len(sys.argv) > 1 else "../../models/mobilenetv2_rk3588_fp.rknn"
IMAGE = sys.argv[2] if len(sys.argv) > 2 else "test_zebra.jpg"
LABELS = "synset.txt"


def softmax(x):
    x = x - np.max(x)
    e = np.exp(x)
    return e / np.sum(e)


def main():
    with open(LABELS) as fh:
        labels = [line.rstrip("\n") for line in fh]

    img = cv2.imread(IMAGE)
    if img is None:
        raise SystemExit("cannot read image: %s" % IMAGE)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, 0)  # NHWC uint8

    rknn = RKNNLite()
    if rknn.load_rknn(MODEL) != 0:
        raise SystemExit("load_rknn failed: %s" % MODEL)
    if rknn.init_runtime(core_mask=RKNNLite.NPU_CORE_0_1_2) != 0:
        raise SystemExit("init_runtime failed")
    outputs = rknn.inference(inputs=[img])
    rknn.release()

    scores = softmax(np.squeeze(outputs[0]).astype(np.float32))
    top5 = np.argsort(scores)[::-1][:5]
    print("-----TOP 5-----")
    for i in top5:
        print('[%d] score=%.4f class="%s"' % (i, scores[i], labels[i]))


if __name__ == "__main__":
    main()
