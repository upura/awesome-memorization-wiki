---
title: 暗記の 3 因子のうち、日本語で崩れるのはどれか
date: 2026-07-29
type: query
tags: [japanese, empirical]
---

# Q. 暗記の 3 因子（重複・モデルサイズ・文脈長）のうち、日本語で崩れるのはどれか

## A. 文脈長だけが崩れる

| 因子 | 日本語 | 他の低資源言語 | 根拠 |
|---|---|---|---|
| [文字列の重複](../concepts/string-duplication.md) | **再現** | — | [Kiyomaru 24](../papers/kiyomaru-2024-comprehensive-analysis.md) / [Ishihara 24](../papers/ishihara-2024-japanese-newspaper.md) / [Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) |
| [モデルサイズ](../concepts/model-size.md) | **再現** | **再現** | [Kiyomaru 24](../papers/kiyomaru-2024-comprehensive-analysis.md) / [Satvaty 25](../papers/satvaty-2025-language-sensitive.md) |
| [文脈長](../concepts/context-length.md) | **逆転** | — | [小柳 24]、[Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md)（一部の実験） |

英語での原典はいずれも [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md)。

## なぜこの問いをファイリングしたか

[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 7·2 節は
「暗記の普遍的要因と文脈依存的要因を切り分ける研究が期待される」と述べるが、
**現時点でどこまで切り分けられているかは 4·4 節と 7·2 節に分散していて一覧できない**。
3 つの概念ページと 4 つの論文ページを突き合わせて初めて上の表になる。

この整理は [ドメインや言語横断](../concepts/multilingual-and-domain.md) の `## 横断的知見` に還元済み。

## 逆転の原因として切り分けられていない候補

1. **言語特性** — 日本語には語境界が無い。トークナイザとしてユニグラム言語モデル
   [Kudo 18] が普及しており、トークン分割が影響する可能性
   [Ippolito 23](../papers/ippolito-2023-false-sense-of-privacy.md)
2. **定量化手法** — 反例はいずれも [メンバーシップ推論](../concepts/membership-inference.md) の設定である。
   日本語で[文字列類似度](../concepts/string-similarity-memorization.md)ベースの文脈長分析が
   同様に行われたかは、この Wiki では未確認
3. **ドメイン** — [Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) は
   継続事前学習という特殊な設定
4. **評価セットの構成** — [Das 25](../papers/das-2025-blind-baselines.md) が示したように、
   メンバーシップ推論の性能は正例・負例の分布差に強く影響される。
   「文脈長が短いほど性能が高い」が暗記ではなく分布差の検出しやすさを
   反映している可能性（推測）→ [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## 次に調べるべきこと

- **[Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) を ingest する。**
  逆転が「一部の実験で」観測された点が鍵で、
  再現しなかった実験との差が候補 1〜4 のどれを支持するかが分かる可能性がある
- 日本語で文字列類似度ベースの文脈長分析を行った研究を探す。
  あれば候補 2 を検証できる（Wiki 未回答）
- 中国語・タイ語など、語境界の無い他言語での報告を探す。候補 1 の検証

## Wiki 内の接点

[文脈長](../concepts/context-length.md) / [ドメインや言語横断](../concepts/multilingual-and-domain.md) / [文字列の重複](../concepts/string-duplication.md) / [モデルサイズ](../concepts/model-size.md)
