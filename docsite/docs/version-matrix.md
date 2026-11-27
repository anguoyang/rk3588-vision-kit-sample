# Version Matrix

Every artifact and number in this kit is tied to the combination below.
This is the single most valuable page in the documentation: RKNN deployment
failures are overwhelmingly version-mismatch failures.

## Tested configuration (reference)

| Component | Version | Notes |
|---|---|---|
| SoC | Rockchip RK3588 | NPU 6 TOPS, driver-visible as `RKNPU` |
| Board OS | Ubuntu 22.04.5 LTS | |
| Kernel | 6.1.118 | |
| NPU driver | 0.9.8 | `dmesg \| grep -i rknpu` |
| Runtime (`librknnrt`) | 2.3.2 | build `429f97ae6b@2025-04-09` |
| Conversion toolkit | rknn-toolkit2 2.3.2 | x86_64 host only; does not run on the board |
| Host Python | 3.10–3.12 | conversion environment |
| Board Python | 3.10 | `pybind` RKNNLite2 matching runtime 2.3.2 |

## Rules that come from hard experience

!!! warning "Toolkit and runtime move together"
    Artifacts converted with toolkit 2.3.2 are verified against runtime
    2.3.2. Mixing a 2.3.x toolkit with a 2.0/2.1 runtime (or the reverse)
    produces load errors or silent accuracy loss. The kit pins the pair.

!!! note "The toolkit is x86_64 only"
    Conversion happens on an x86_64 host. The board only runs artifacts.
    The pipeline scripts in the package assume this split.

!!! note "Runtime is not redistributed"
    `librknnrt` is Rockchip-proprietary. The kit ships sideload instructions
    and version checks, not the binary.

## Support boundary

Support covers configurations inside this matrix. Outside it, the
documentation still applies as guidance, but results are not guaranteed —
start from the [FAQ](faq.md) self-check list before contacting support.
