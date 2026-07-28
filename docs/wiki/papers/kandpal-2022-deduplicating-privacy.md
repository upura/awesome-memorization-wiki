---
title: Deduplicating training data mitigates privacy risks in language models
authors: [Nikhil Kandpal, Eric Wallace, Colin Raffel]
year: 2022
venue: ICML 2022, Vol. 162, pp. 10697–10707
citekey: Kandpal 22
tags: [mitigation, deduplication, privacy, training-set]
axis: [訓練セット]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Deduplicating training data mitigates privacy risks in language models

## TL;DR

重複排除が**プライバシリスク**を緩和することを示した。
[Lee 22](lee-2022-deduplicating.md) が性能向上を論じたのに対し、こちらは漏洩リスクを論じる。

## 位置づけ

訓練セット軸の前処理（[Ishihara 26](ishihara-2026-memorization-survey.md) 5·1）。
[文字列の重複](../concepts/string-duplication.md) の実証にも寄与しており、暗記を**文書単位**で議論している点が特徴
（トークン単位で議論する [Tirumala 22] と対比される）。

## 手法・実験

[逐語暗記](../concepts/string-similarity-memorization.md)の定義を採用。文書単位での議論。
サーベイからは実験設定の詳細は判明しない（原論文未読）。

## 主要な知見

- 重複排除がプライバシリスクを緩和する
- [Carlini 23b](carlini-2023-quantifying-memorization.md) の 3 因子のうち、
  [文字列の重複](../concepts/string-duplication.md) と [文脈長](../concepts/context-length.md) について同様の結果を報告している
- **訓練データ抽出とモデル反転攻撃 [Fredrikson 15] はほぼ同一の攻撃**と位置づけた
  （サーベイ 7·3 節が引用）→ [研究領域の拡張](../concepts/multimodal-memorization.md)

## 限界・批判

- [Lee 22](lee-2022-deduplicating.md) と同じく、重複以外の要因による暗記は防げない
- 文書単位の重複排除は、同じ個人情報が異なる文書に現れる場合には効かない。
  これは[差分プライバシ](../concepts/differential-privacy.md)の粒度問題と同型である → [重複排除](../concepts/deduplication.md)

## Wiki 内の接点

- [重複排除](../concepts/deduplication.md) / [文字列の重複](../concepts/string-duplication.md) / [文脈長](../concepts/context-length.md)
- 姉妹研究: [Lee 22](lee-2022-deduplicating.md)
- 攻撃の歴史的位置づけ: [研究領域の拡張](../concepts/multimodal-memorization.md) / [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md)
