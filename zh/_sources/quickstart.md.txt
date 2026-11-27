# 快速上手（免费样本）

免费样本包含本套件一条完整可运行的切片：MobileNetV2 分类，FP 与
INT8，端到端。它的用途是让你在花钱之前，先验管线、验文档风格、验
数据格式。

## 1. 准备运行时

套件不分发 Rockchip 的专有运行时。用板卡厂商的包安装
`librknnrt` 2.3.2，然后验证：

```bash
strings /usr/lib/librknnrt.so | grep -i "librknnrt version"
# 应输出：librknnrt version: 2.3.2
```

只有[版本矩阵](version-matrix.md)中的组合经过测试。

## 2. 运行样本

```bash
git clone https://github.com/anguoyang/rk3588-vision-kit-sample
cd rk3588-vision-kit-sample/example_classify_mobilenetv2
python3 run_classify.py --model ../models/mobilenetv2_rk3588_fp.rknn --image zebra.jpg
python3 run_classify.py --model ../models/mobilenetv2_rk3588_int8.rknn --image zebra.jpg
```

参考板上的预期输出：

```
top-1: zebra  0.9993   (FP)
top-1: zebra  0.9993   (INT8)
```

## 3. 核对数字

把你的板卡结果与[基准数据](benchmarks.md)的参考值对照。参考配置下
MobileNetV2 为 **p50 8.63 ms（FP）**、**p50 4.15 ms（INT8）**。第一次
运行慢约 15% 是已知的平台效应，不是故障——见
[已知问题](known-issues.md)。

## 下一步

- 完整套件另加 11 件产物、检测/人脸/OCR 示例、自带模型的转换管线
  和全量原始报告。
- 疑问见[常见问题](faq.md)。
