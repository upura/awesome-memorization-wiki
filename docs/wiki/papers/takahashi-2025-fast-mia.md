---
title: "Fast-MIA: Efficient and scalable membership inference for LLMs"
authors: [Shotaro Ishihara, Hiromu Takahashi]
year: 2025
venue: arXiv 2510.23074
citekey: Takahashi 25a
url: https://arxiv.org/abs/2510.23074
tags: [tool, membership-inference, reproducibility]
axis: [出力]
type: paper
---

# Fast-MIA: Efficient and scalable membership inference for LLMs

## TL;DR

メンバーシップ推論の評価を効率化する **Python ライブラリ**（<https://github.com/Nikkei/fast-mia>）。
**vLLM による高スループット推論で約 5 倍**、
さらに**手法をまたいだキャッシュ**で対数尤度などの中間結果を 1 度だけ計算して共有する。

## 位置づけ

出力軸。[評価セットとライブラリ](../concepts/benchmarks-and-tools.md)に属する実装で、
サーベイ 3·2§2 が挙げるライブラリの一つ。

**この Wiki で唯一、手法や知見ではなく「研究のインフラ」を扱うページ**である。

## 手法・実験

計算効率化の 2 戦略:

1. **vLLM による高スループットなバッチ推論** — 約 5 倍の高速化
2. **手法横断のキャッシュ機構** — 対数確率などの共有される中間結果を一度だけ計算し、
   複数手法で使い回す

## 主要な知見

### なぜ効率が問題になったか

論文が挙げる 2 つの潮流が、計算効率を**研究のボトルネック**にした。

- **多パス推論の手法が増えた。** ReCaLL [Xie 24b] や Con-ReCall [Wang 25a] は
  複数の接頭辞構成で損失を計算する必要があり、SaMIA [Kaneko 25b] のような
  ブラックボックス手法はサンプルごとに多数の生成を要する
  → [メンバーシップ推論](../concepts/membership-inference.md)
- **データセット規模の評価が必須になった。** [Puerto 25] は、
  メンバーシップ推論が**個々の文ではなく複数文書にまたがって集約したときに初めて有効になる**
  ことを示し、焦点を文単位から**コレクション単位**へ移した
  → [データセット汚染](../concepts/data-contamination.md)

### 既存実装の非効率

既存の実装は各手法を独立に実行するため、
**対数確率のような共有される中間結果を冗長に計算していた**。

## 限界・批判

- ライブラリであり、新しい知見や手法を提案するものではない
- 高速化は評価セットの妥当性の問題（[Das 25](das-2025-blind-baselines.md)）を解決しない。
  **壊れた評価を速く回せるようになるだけ**である。
  ただし大規模な再評価が現実的になることで、
  MIMIR / OLMoMIA 上での体系的な再ランキングという未解決課題には資する
- 対応手法の網羅性はこの Wiki では未確認

## Wiki 内の接点

- [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- [データセット汚染](../concepts/data-contamination.md)（コレクション単位の評価）
- 同著者: [Ishihara 24](ishihara-2024-japanese-newspaper.md) / [Takahashi 25b](takahashi-2025-continual-pretraining-japanese.md) / [Ishihara 26](ishihara-2026-memorization-survey.md)
