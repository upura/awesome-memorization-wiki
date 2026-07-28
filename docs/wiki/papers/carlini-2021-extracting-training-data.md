---
title: Extracting training data from large language models
authors: [Nicholas Carlini, Florian Tramèr, Eric Wallace, et al.]
year: 2021
venue: USENIX Security 21, pp. 2633–2650
citekey: Carlini 21
tags: [extraction, membership-inference, privacy, landmark]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Extracting training data from large language models

## TL;DR

GPT-2 [Radford 19] から**暗記された個人情報が検出できる**と警鐘を鳴らした先駆的研究。
候補生成 + [メンバーシップ推論](../concepts/membership-inference.md)という 2 段階の訓練データ抽出手続きを確立した。

## 位置づけ

出力軸。この分野の起点となる論文であり、[Ishihara 26](ishihara-2026-memorization-survey.md) 冒頭で
「先駆的な研究」として紹介される。
[逐語暗記](../concepts/string-similarity-memorization.md)の定義もここから広く採用された。

## 手法・実験

**訓練データ抽出の 2 段階**（サーベイ 6·1 節が整理）:

1. **候補生成** — 訓練データの候補となるテキストを大量に生成する
2. **メンバーシップ推論** — 生成された候補が訓練セットに含まれるかを判定する

あわせて、後続で標準的に使われる指標を提示した:

- **PPL/zlib** — zlib 圧縮で計算される情報量で PPL を割る。訓練セット外のテキストは
  生成確率が低く、繰り返しなど冗長な表現が現れるため圧縮されやすい、という仮説に基づく
- **Lowercase** — 入力テキストを全て小文字に変換する前後で PPL を比較する。
  大文字・小文字といったモデルに暗記されやすい**表層的な特徴**を利用する

## 主要な知見

- 事前学習済み言語モデルから個人情報が実際に抽出できる
- 学習の進展の中で、特定の訓練データが**異常に低い損失**を示すことを観測した
  （→ [学習順と忘却](../concepts/training-order-and-forgetting.md)）
- 明示的に公開されていなくても「Bob's phone number is」「Alice's password is」といった
  推察も可能である [Carlini 19, Henderson 18]

## 限界・批判

- 抽出できたことは示すが、**どの程度深刻か**（許容可能な暗記との区別）は扱っていない。
  [Lee 20] の批判が該当する → [評価の枠組み](../concepts/evaluation-framework.md)
- PPL/zlib・Lowercase は基礎的手法としてよく用いられる [Chen 25] が、
  その後の評価セットの分布差問題（→ [評価セットとライブラリ](../concepts/benchmarks-and-tools.md)）の影響を受ける

## Wiki 内の接点

- [暗記](../concepts/memorization.md) / [セキュリティと情報漏洩](../concepts/security-and-privacy-leakage.md) / [メンバーシップ推論](../concepts/membership-inference.md)
- 定量的な後継: [Carlini 23b](carlini-2023-quantifying-memorization.md)
- 評価指標への自己批判: [Carlini 22](carlini-2022-first-principles.md)
- 本論文を引用している概念: [学習過程における抑制](../concepts/mitigation-in-training.md)
