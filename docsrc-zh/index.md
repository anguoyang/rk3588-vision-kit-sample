# RK3588 视觉部署套件

**省掉那两周的搭建时间。** 本套件是一条经过实机验证的 ONNX → RKNN 部署
管线，面向 Rockchip RK3588：转换好的模型产物、实测过的版本矩阵、逐算子
的 CPU 回退数据，以及在真实硬件上测得的数据——不是模拟器，不是抄自数据
手册。

本站文档**免费且完整**。请先读完、核对数字、跑通免费样本。付费包里是可
运行的产物、全量原始测量数据和调好的转换脚本。

## 内容对照

| | 免费（本站＋样本仓） | Starter（$79） | Complete（$149） |
|---|---|---|---|
| 完整文档（方法、矩阵、结果、失败记录） | ✅ | ✅ | ✅ |
| MobileNetV2 端到端样本（FP＋INT8 产物） | ✅ | ✅ | ✅ |
| 转换管线（全部模型） | — | ✅ | ✅ |
| 12 件转换产物（FP＋INT8） | — | ✅ | ✅ |
| 示例工程（分类、检测、人脸） | — | ✅ | ✅ |
| OCR＋自带模型示例 | — | — | ✅ |
| 全量原始测量报告（25 份） | — | — | ✅ |
| 转换笔记与标定细节 | — | — | ✅ |
| 更新期 | — | 6 个月 | 12 个月 |

## 测量环境

本站全部数字在同一套有据可查的配置上测得：

- **SoC／板卡：** Rockchip RK3588
- **系统：** Ubuntu 22.04.5 LTS，内核 6.1.118
- **运行时：** librknnrt 2.3.2 · **驱动：** rknpu 0.9.8
- **转换：** rknn-toolkit2 2.3.2（x86_64 主机）

确切的版本组合见[版本矩阵](version-matrix.md)，测量协议见
[基准数据](benchmarks.md)。矩阵之外测得的数字，出现时都会明确标注。

## 为什么不自己做？

可以做，官方指南也是免费的。但它不给你这些：

- **已在硬件上验过的产物**，带 SHA-256 哈希。
- **失败记录**——哪种 INT8 标定会悄悄压垮检测器的置信度、哪个产物会
  因为编译器内存规划问题膨胀到 18 MB、哪些算子回退到 CPU 且占比多少。
  见[已知问题](known-issues.md)。
- **一整套确定能协同工作的版本矩阵**，而不是三天耗在工具链/驱动/运行时
  版本不匹配上。

这个包卖的就是这个：那两周，已经替你花掉了。

## 购买

- Starter $79 · Complete $149，Gumroad（EdgeModelLab 店）
- 免费样本：上方链接的 GitHub 仓（MobileNetV2 全管线）
- 支持与 14 天退款（在版本矩阵配置内按文档跑不通可全额退）：见
  [常见问题](faq.md)。

```{toctree}
:hidden:
:maxdepth: 2

quickstart
version-matrix
benchmarks
known-issues
faq
```

```{raw} html
<p><strong>语言：</strong> <a href="../" onclick="sessionStorage.setItem('lang-chosen','1')">English</a> &middot; 简体中文 &middot; <a href="../ja/" onclick="sessionStorage.setItem('lang-chosen','1')">日本語</a></p>
```
