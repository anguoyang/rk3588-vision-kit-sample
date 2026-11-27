# Known Issues & Failure Records

This page is the part you cannot get from a model zoo or an AI assistant:
things that actually went wrong on real hardware, how they were diagnosed,
and what ships instead. It is updated whenever a measurement contradicts a
previous claim.

## First-context effect

The first RKNN process after the board has been idle measures **~15%
slower**, even after warmup runs, on RK3588 with the `rknpu_ondemand`
governor. A single quick benchmark right after boot will systematically
understate the board.

**Kit protocol:** one sacrificial load + 5-run cycle in a separate process
before any timed session (see [Benchmarks](benchmarks.md#protocol)). If your
numbers are ~15% below this site's and you benchmarked once, cold, this is
almost certainly why.

## RetinaFace INT8

Two separate problems, both reproduced:

1. **Artifact bloat.** The toolkit 2.3.2 build of this model produced an
   18.9 MB artifact for a ~1.5 M-parameter network. Layer isolation traced it
   to memory planning around the final `Concat` operator: roughly 17.5 MB of
   zero-filled image is written into the artifact. It is a compiler
   behaviour, not a settings error, and cannot be tuned away from the user
   side.
2. **Confidence collapse with `normal` calibration.** The normally-calibrated
   INT8 build systematically compresses detection confidence: at a 0.5
   threshold it detected **0 of 3** faces in the reference scene. The
   KL-divergence calibrated build detects 2 of 3 at the same threshold, but
   remains slower than the FP build (7.99 ms vs 6.43 ms p50) with a 2.74%
   CPU-fallback share.

**What ships:** the FP artifact is the recommended RetinaFace build. The
KL-calibrated INT8 artifact is included as a measurement record with this
page as its documentation. The `normal`-calibration build was withdrawn.

## PP-OCRv4-Rec Reshape fallback

Both FP and INT8 builds of the recognition model execute one `Reshape`
(after the final softmax) on CPU: 2.58% / 2.61% of frame time. It does not
block deployment; it is recorded so your latency budget is honest.

## Session variance

Session medians for the same artifact can differ visibly (e.g. YOLO11n INT8
session p50 values of 23.8 / 31.4 / 31.2 ms in one measurement set). The kit
reports the median of three sessions and keeps the per-session values in the
raw reports (Complete package) — if a vendor table shows you one number with
no spread, ask how it was measured.
