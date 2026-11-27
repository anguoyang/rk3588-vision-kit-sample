# クイックスタート（無料サンプル）

無料サンプルには、本キットの完全で実行可能な一切れ——MobileNetV2 の
分類、FP と INT8、エンドツーエンド——が入っています。お金を払う前に、
パイプライン、ドキュメントの書き方、データ形式を検証するための
ものです。

## 1. ランタイムを用意する

本キットは Rockchip のプロプライエタリなランタイムを再配布しません。
ボードベンダのパッケージで `librknnrt` 2.3.2 をインストールし、
確認してください。

```bash
strings /usr/lib/librknnrt.so | grep -i "librknnrt version"
# 期待値：librknnrt version: 2.3.2
```

テスト済みなのは[バージョン対応表](version-matrix.md)の組み合わせ
だけです。

## 2. サンプルを実行する

```bash
git clone https://github.com/anguoyang/rk3588-vision-kit-sample
cd rk3588-vision-kit-sample/example_classify_mobilenetv2
python3 run_classify.py --model ../models/mobilenetv2_rk3588_fp.rknn --image zebra.jpg
python3 run_classify.py --model ../models/mobilenetv2_rk3588_int8.rknn --image zebra.jpg
```

リファレンスボードでの期待出力：

```
top-1: zebra  0.9993   (FP)
top-1: zebra  0.9993   (INT8)
```

## 3. 数値を確認する

お使いのボードの結果を[ベンチマーク](benchmarks.md)のリファレンス値と
比べてください。リファレンス構成では MobileNetV2 は **p50 8.63 ms
（FP）**、**p50 4.15 ms（INT8）** です。初回実行が約15%遅いのは
既知のプラットフォーム特性で、故障ではありません——
[既知の問題](known-issues.md)参照。

## 次のステップ

- フルキットには、さらに11点の成果物、検出/顔/OCR のサンプル、自前
  モデル用変換パイプライン、生レポート全量が入ります。
- 質問は[FAQ](faq.md)へ。
