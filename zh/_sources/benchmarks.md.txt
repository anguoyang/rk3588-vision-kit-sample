# 基准数据

## 测量协议

下表每个数字都按同一套协议、在[参考配置](version-matrix.md)上测得：

- **预热：** 10 次；随后每会话 **50 次计时运行**
- **会话：** 3 个独立会话，各自独立进程；报告值为**三会话中位数的
  中位数**
- **预热引子：** 测量前先在一个单独进程里做一次牺牲性的加载＋5 次
  运行（原因见[已知问题](known-issues.md)的「首次上下文效应」）
- **计时：** NPU `PERF_RUN` 剖析；CPU 回退占比由逐算子计时算出
- **判定：** `NPU_ONLY` = 无算子在 CPU 上执行；`MIXED` = 有算子回退
  （占比列出）

这块 SoC 上单会话数字可以偏离持续状态约 15%——所以要对比，先照
这个协议测。

## 结果（23 个测量配置，14 个模型）

| 模型 | 任务 | 精度 | p50 (ms) | p95 (ms) | FPS (p50) | 判定 | CPU 回退 |
|---|---|---|---|---|---|---|---|
| MobileNetV2 | 分类 | FP | 8.63 | 8.89 | 115.9 | NPU_ONLY | 0% |
| MobileNetV2 | 分类 | INT8 | 4.15 | 4.65 | 241.3 | MIXED | 1.10% |
| ResNet50-v2 | 分类 | FP | 25.40 | 29.34 | 39.4 | NPU_ONLY | 0% |
| ResNet50-v2 | 分类 | INT8 | 13.54 | 15.26 | 73.8 | MIXED | 0.63% |
| RetinaFace (Mobile320) | 人脸检测 | FP | 6.43 | 6.68 | 155.6 | MIXED | 4.05% |
| RetinaFace (Mobile320) | 人脸检测 | INT8 | 7.99 | 8.35 | 125.2 | MIXED | 2.74% |
| YOLO11n | 检测 | FP | 43.67 | 49.79 | 22.9 | NPU_ONLY | 0% |
| YOLO11n | 检测 | INT8 | 31.20 | 31.69 | 32.1 | NPU_ONLY | 0% |
| YOLOv5s (ReLU) | 检测 | FP | 37.81 | 38.58 | 26.5 | NPU_ONLY | 0% |
| YOLOv5s (ReLU) | 检测 | INT8 | 20.52 | 22.30 | 48.7 | NPU_ONLY | 0% |
| YOLOv8n | 检测 | FP | 37.50 | 38.58 | 26.7 | NPU_ONLY | 0% |
| YOLOv8n | 检测 | INT8 | 19.17 | 19.76 | 52.2 | NPU_ONLY | 0% |
| YOLOv10s | 检测 | FP | 88.09 | 90.49 | 11.4 | NPU_ONLY | 0% |
| YOLOv8n-obb | 旋转框检测 | FP | 37.65 | 38.26 | 26.6 | NPU_ONLY | 0% |
| YOLOv8n-pose | 姿态 | FP | 49.74 | 51.27 | 20.1 | NPU_ONLY | 0% |
| YOLOv8n-pose | 姿态 | INT8 | 31.64 | 32.71 | 31.6 | NPU_ONLY | 0% |
| YOLOv8n-seg | 分割 | FP | 46.74 | 57.36 | 21.4 | NPU_ONLY | 0% |
| YOLOv8s-seg | 分割 | FP | 104.54 | 113.09 | 9.6 | NPU_ONLY | 0% |
| YOLOv8s-seg | 分割 | INT8 | 43.84 | 45.44 | 22.8 | NPU_ONLY | 0% |
| PP-YOLOE-s | 检测 | FP | 67.71 | 70.44 | 14.8 | NPU_ONLY | 0% |
| PP-YOLOE-s | 检测 | INT8 | 35.80 | 36.42 | 27.9 | NPU_ONLY | 0% |
| PP-OCRv4-Det | 文字检测 | FP | 47.86 | 49.99 | 20.9 | NPU_ONLY | 0% |
| PP-OCRv4-Det | 文字检测 | INT8 | 31.39 | 39.99 | 31.9 | NPU_ONLY | 0% |
| PP-OCRv4-Rec | 文字识别 | FP | 22.68 | 26.45 | 44.1 | MIXED | 2.58% |
| PP-OCRv4-Rec | 文字识别 | INT8 | 14.16 | 16.96 | 70.6 | MIXED | 2.61% |

## 这张表怎么读

- **INT8 不一定更快。** RetinaFace 的 INT8 在这套栈上比 FP 还慢，
  随包的是测量记录，推荐用 FP 件。细节见[已知问题](known-issues.md)。
- **MIXED 不是坏事。** 少数 `Reshape` 算子回退 CPU 是常态，关键看
  占比——每个模型都印出来了，多数厂商的表会把这一列省掉。
- **全量原始报告**（逐算子计时、内存增量、逐会话数据）在 Complete
  包里。上表摘要完整且免费；原始文件是你拿去支撑采购决策复核的。
