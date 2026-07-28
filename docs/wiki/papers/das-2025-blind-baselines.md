---
title: Blind baselines beat membership inference attacks for foundation models
authors: [Debeshee Das, Jie Zhang, Florian Tramèr]
year: 2025
venue: IEEE Security and Privacy Workshops (SPW) 2025, pp. 118–125
citekey: Das 25
tags: [membership-inference, critique, benchmark]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Blind baselines beat membership inference attacks for foundation models

## TL;DR

WikiMIA では**年の文字列に着目するといった素朴な手法でも、
高度なメンバーシップ推論手法より高い性能が観測される**。
既存の手法比較が暗記ではなく**正例・負例の分布差**を測っていた可能性を示した。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md) の方法論に対する最も直接的な反証。
サーベイ 3·2§2 の評価セット批判の中核。

## 手法・実験

モデルの出力を一切見ない「盲目的（blind）」なベースライン——
たとえばテキストに含まれる年号を見るだけ——を既存手法と比較する。

WikiMIA は Wikipedia を元に、2017 年以前に作成された記事を正例、
評価対象モデル公開後の 2023 年以降に作成された記事を負例としているため、
**時期を示す表層的な手がかりが正解ラベルとほぼ一致してしまう**。

## 主要な知見

- 盲目的なベースラインが既存のメンバーシップ推論手法を上回る
- したがって、WikiMIA 上で報告された性能差は
  **手法の優劣を反映していない可能性がある**

## 限界・批判

- 「既存の評価が壊れている」ことは示すが、正しい評価セットの構築方法を
  与えるわけではない。MIMIR [Duan 24](duan-2024-do-mia-work.md) や OLMoMIA [Kim 26] が
  応答として提案されているが、体系的な再ランキングは
  この Wiki では未確認 → [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)

## Wiki 内の接点

- [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [メンバーシップ推論](../concepts/membership-inference.md) / [評価の枠組み](../concepts/evaluation-framework.md)
- 批判対象: [Shi 24](shi-2024-min-k-prob.md)
- 同方向: [Chen 25](chen-2025-revisiting-mia.md) / [Duan 24](duan-2024-do-mia-work.md) / [Zhang 25a](zhang-2025-mia-cannot-prove.md)
- 著作権立証への含意: [著作権](../concepts/copyright.md)
- 本論文を引用している概念: [データセット汚染](../concepts/data-contamination.md) / [文脈長](../concepts/context-length.md)
