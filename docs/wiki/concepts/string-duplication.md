---
title: 文字列の重複（Duplication）
aliases: [重複, duplication, 重複回数]
axis: 訓練セット
survey_section: "4·1"
tags: [empirical, training-set]
type: concept
---

# 文字列の重複：重複テキストは暗記されやすい

## 定義

訓練セット内で同じ文字列が出現する**回数**。3 つの実証的知見のうち、
**訓練セット軸**に対応するもの（[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 4·1）。

[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) は訓練セット内の文字列の重複回数を
**2 から 900 までの塊に分けて**暗記量を測定し、重複が多いほど暗記されやすいと観測した。

## 主要な論文

- [Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) — 重複回数と暗記量の関係を定量化した原典
- [Lee 22](../papers/lee-2022-deduplicating.md) — 重複排除が言語モデルを良くする。トークン一致率で測定
- [Kandpal 22](../papers/kandpal-2022-deduplicating-privacy.md) — 重複排除がプライバシリスクを緩和する
- [Ishihara 24](../papers/ishihara-2024-japanese-newspaper.md) — 日本語新聞記事で重複に関する知見を再現
- [Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) — 日本語の継続事前学習で再現
- [Chang 23](../papers/chang-2023-speak-memory.md) — 事後学習済みモデル（ChatGPT / GPT-4）でも暗記度合いが Web 上の出現頻度と関連

後続研究で広く再現されている: [Chang 25, Huang 24, Ippolito 23, Ishihara 24, Kandpal 22,
Kiyomaru 24, Lee 22, Lee 23, Lu 24, McCoy 23, Takahashi 25b, Tirumala 22]。

## 横断的知見

**3 因子のうち、最も再現性が高く、最も言語横断で頑健である。**
サーベイ 4 章の 3 因子（重複・[モデルサイズ](model-size.md)・[文脈長](context-length.md)）を
比べると、日本語での検証状況に差がある。
[Ishihara 24](../papers/ishihara-2024-japanese-newspaper.md) と [Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) は
**重複に関する知見を日本語で再現**している。一方 [文脈長](context-length.md) は
[小柳 24] が**逆の関係**を報告している。
つまり重複は言語に依存しにくい普遍的要因、文脈長は文脈依存的要因である可能性が高い。
これはサーベイ 7·2 節が求める「暗記の普遍的要因と文脈依存的要因を切り分ける研究」に
対する、現時点での暫定的な回答になっている。

**メンバーシップ推論の設定でも再現される。** サーベイは重複の知見が
「メンバーシップ推論の設定も含め」後続研究で再現されていると述べる。
定量化手法を変えても生き残る知見は 3 因子の中でこれが最も確かである。
逆に言えば、[メンバーシップ推論](membership-inference.md) の評価セットが[分布差で汚染](benchmarks-and-tools.md)
されていたという批判が正しくても、重複の知見そのものは
[文字列類似度](string-similarity-memorization.md)側の証拠で支えられている。

**「重複が多い＝暗記される」は、暗記と忘却の同時進行として説明できる。**
[Leybzon 24] の解釈: 一度しか出現しない文字列は、一度暗記された後は
**その後の学習ステップで忘却され続ける**。重複が多く出現頻度が高い文字列は、
忘却され続ける中で**複数回の暗記が起こり**、結果的に学習終了後も暗記が保持されやすい。
この解釈は、重複の効果と[学習順の効果](training-order-and-forgetting.md)を
**同一のメカニズムから導く**点で重要である。両者は独立した 2 つの現象ではない。

**したがって重複排除は根本的な解決にならない。** サーベイ 5·1 節が明記するとおり、
**重複以外の要因でも暗記は発生し得るため、重複排除のみで完全に防ぐことはできない**。
[重複排除](deduplication.md) は最も費用対効果の高い緩和策だが、上限がある。

## 未解決の問い

- 重複の「単位」はトークンか、文書か、意味的に等価な言い換えを含むか。
  [Tirumala 22] はトークン、[Kandpal 22] は文書で議論しており統一されていない
- 日本語のように語境界が無い言語では、トークナイザ [Kudo 18] の分割方針が
  重複のカウントに影響する可能性がある [Ippolito 23] → [ドメインや言語横断](multilingual-and-domain.md)
- 重複回数と暗記量の関数形（対数線形か、閾値的か）はドメインによらず一定か
- [Leybzon 24] の暗記・忘却モデルは、バッチサイズや学習率スケジュールを変えても成立するか
