---
title: "Training data extraction from pre-trained language models: A survey"
authors: [Shotaro Ishihara]
year: 2023
venue: 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023), pp. 260–275
citekey: Ishihara 23
url: https://aclanthology.org/2023.trustnlp-1.23/
tags: [survey, extraction]
axis: [出力]
type: paper
---

# Training data extraction from pre-trained language models: A survey

## TL;DR

事前学習済み言語モデルからの**訓練データ抽出**に関する初の包括的サーベイ。
[Carlini 21](carlini-2021-extracting-training-data.md) を引用する 100 本超を体系化し、
暗記の定義の分類・攻撃と防御・実証的知見・今後の方向性を整理した。
[Ishihara 26](ishihara-2026-memorization-survey.md) の前身。

## 位置づけ

出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) は本論文の**発展版**であり、
「その後の研究動向を踏まえて内容を再構成・追記した」と明記されている。

2023 → 2026 での主な拡張:

| 観点 | 2023（本論文） | 2026 |
|---|---|---|
| 対象 | 訓練データ**抽出** | **暗記**全般 |
| 体系 | 定義の分類 / 攻撃・防御 / 実証的知見 | **訓練セット・モデル・出力の 3 軸** |
| モデル軸の定義 | — | [反実仮想](../concepts/counterfactual-memorization.md)・[差分プライバシ](../concepts/differential-privacy.md)を明示的に整理 |
| 社会的課題 | — | [著作権](../concepts/copyright.md)・[評価の正当性](../concepts/data-contamination.md)（6 章） |
| 文献数 | 100 本超 | 約 180 本 |

## 手法・実験

サーベイ論文。**[Carlini 21](carlini-2021-extracting-training-data.md) を引用する論文を、
関係性・被引用数・採択状況で選別**するという明示的な手続きで文献を収集している。
起点となる 1 本から前向きに辿る方法であり、この分野が単一の論文から急速に広がったことを反映する。

## 主要な知見

- **暗記の定義の分類法**を提示した（3 章）
- **訓練データ抽出は、セキュリティ分野で知られるモデル反転攻撃
  [Fredrikson 15] に近づいている**と位置づけた。
  この視点は [Ishihara 26](ishihara-2026-memorization-survey.md) 7·3 節にも引き継がれ、
  [Kandpal 22](kandpal-2022-deduplicating-privacy.md) の
  「両者はほぼ同一の攻撃」という評価と一致する → [研究領域の拡張](../concepts/multimodal-memorization.md)
- 攻撃と防御の手法を体系化した
- 複数の定量的研究の実証的知見を整理した

## 限界・批判

- 2023 年前半までの文献に基づく。[Shi 24](shi-2024-min-k-prob.md) 以降の
  [メンバーシップ推論](../concepts/membership-inference.md)の展開と、
  その方法論的批判（[Das 25](das-2025-blind-baselines.md) など）は含まない
- 対象を訓練データ**抽出**に絞っており、
  [知識を問うタスク](../concepts/knowledge-probing.md)や
  [データセット汚染](../concepts/data-contamination.md)は扱いが薄い
- 文献の選別が [Carlini 21](carlini-2021-extracting-training-data.md) の被引用に依拠するため、
  この系譜の外にある研究（[反実仮想](../concepts/counterfactual-memorization.md)など）が
  拾われにくい構造がある（推測）

## Wiki 内の接点

- 発展版: [Ishihara 26](ishihara-2026-memorization-survey.md)
- [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) / [暗記](../concepts/memorization.md)
- [研究領域の拡張](../concepts/multimodal-memorization.md)（モデル反転攻撃との接続）
- 起点となった論文: [Carlini 21](carlini-2021-extracting-training-data.md)
