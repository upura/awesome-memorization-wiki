---
title: "Speak, memory: An archaeology of books known to ChatGPT/GPT-4"
authors: [Kent Chang, Mackenzie Cramer, Sandeep Soni, et al.]
year: 2023
venue: EMNLP 2023, pp. 7312–7327
citekey: Chang 23
tags: [knowledge-probing, post-training, copyright, output]
axis: [出力]
type: paper
stub: true
source_note: サーベイ [Ishihara 26] 経由（原論文未読）
---

# Speak, memory: An archaeology of books known to ChatGPT/GPT-4

## TL;DR

訓練データの一部が欠損した入力に対して、モデルが**欠損部分を復元できるか**を測定し、
ChatGPT / GPT-4 が知っている書籍を推定した。
事後学習済みモデルでも暗記度合いが **Web 上の出現頻度**と関連していることを報告。

## 位置づけ

出力軸。[知識を問うタスク](../concepts/knowledge-probing.md)による暗記の定量化の代表例
（[Ishihara 26](ishihara-2026-memorization-survey.md) 3·2§3）。

**この Wiki で、事後学習済みの実用モデルを対象にした数少ない研究である。**
サーベイは 3〜5 章で原則としてベースモデルを扱うが、本研究は例外的に
ChatGPT / GPT-4 [OpenAI 23] を扱う。

## 手法・実験

訓練データの一部を欠損させた入力（cloze 形式）を与え、
モデルが欠損部分を復元できるかを測定する。
生成確率へのアクセスも訓練セットの知識も不要で、API 越しの入出力だけで成立する。

## 主要な知見

- ChatGPT や GPT-4 といった**事後学習を施したモデルでも**、
  暗記度合いが Web 上に出現する頻度と関連している
  → [文字列の重複](../concepts/string-duplication.md) の知見が事後学習済みモデルでも成立する

## 限界・批判

- 「知っている / 知らない」の二値判定であり、
  [Chang 25] のような意味的汎化・構成的汎化の段階は扱わない
  → [暗記と汎化](../concepts/memorization-vs-generalization.md)
- 知識を問うタスクは暗記の測定器であると同時に、
  暗記によって汚染される対象でもある → [データセット汚染](../concepts/data-contamination.md)

## Wiki 内の接点

- [知識を問うタスク](../concepts/knowledge-probing.md) / [文字列の重複](../concepts/string-duplication.md) / [暗記](../concepts/memorization.md)
- [著作権](../concepts/copyright.md)（書籍という著作物を対象にしている）
- [データセット汚染](../concepts/data-contamination.md)
