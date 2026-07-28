---
title: "Training data extraction from pre-trained language models: A survey"
authors: [Shotaro Ishihara]
year: 2023
venue: 3rd Workshop on Trustworthy Natural Language Processing (TrustNLP 2023), pp. 260–275
citekey: Ishihara 23
tags: [survey, extraction]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Training data extraction from pre-trained language models: A survey

## TL;DR

[Ishihara 26](ishihara-2026-memorization-survey.md) の**前身**にあたるサーベイ（2023 年 7 月公開）。
訓練データ抽出に焦点を当てている。

## 位置づけ

出力軸。[Ishihara 26](ishihara-2026-memorization-survey.md) は本論文の**発展版**であり、
「その後の研究動向を踏まえて内容を再構成・追記した」と明記されている。

2023 → 2026 での主な拡張（サーベイ本文から読み取れる範囲）:

- 対象が「訓練データ抽出」から「暗記」全般へ広がった
- **訓練セット・モデル・出力**という 3 軸の体系が導入された
- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) や [差分プライバシ](../concepts/differential-privacy.md) といった
  モデル軸の定義が明示的に整理された
- [評価の正当性](../concepts/data-contamination.md)・[著作権](../concepts/copyright.md)など社会的課題（6章）と
  展望（7章）が加わった

## 手法・実験

サーベイ論文。

## 主要な知見

**要 ingest。** 2023 年時点での訓練データ抽出研究の整理。

## 限界・批判

- 2023 年 7 月時点の文献に基づく。[Shi 24](shi-2024-min-k-prob.md) 以降の
  メンバーシップ推論の展開と、その方法論的批判
  （[Das 25](das-2025-blind-baselines.md) など）は含まない

## Wiki 内の接点

- 発展版: [Ishihara 26](ishihara-2026-memorization-survey.md)
- [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) / [暗記](../concepts/memorization.md)
