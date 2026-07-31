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

**言語には頑健だが、データセットには頑健でない。** この非対称が本ページの核心である。
サーベイの記述だけを読むと重複は最も確立した因子に見えるが、
原典の追試節（[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) 5 章）は
**重複の知見がモデル族・データセットを跨ぐと崩れる**と明示している。

> We expected our results to cleanly generalize across settings, and this is indeed true for
> **model scale**. Yet, the situation is more complicated when considering **data duplication**,
> due to training set idiosyncrasies.

| 設定 | 重複の効果 |
|---|---|
| GPT-Neo / Pile（主実験） | 対数線形。2〜900 回で単調に増加 |
| **T5 / C4**（マスク型） | **単調でない。** 138〜158 回重複が 159〜196 回重複より暗記されやすい（3σ で有意）。原因は前者が空白トークン主体で予測しやすいこと |
| **OPT / 整理済み Pile** | 傾向は同じだが**効果の大きさが数桁小さい**。66B OPT が 125M GPT-Neo より暗記が少ない |

T5 の非単調性は、**重複回数が「暗記のされやすさ」の代理変数として不完全**であることを示す。
実際に効いているのは重複そのものではなく**予測の容易さ**であり、
重複はその相関物にすぎない可能性がある。この読みは
[Leybzon 24] の忘却モデル（後述）とも整合する。

**一方、言語を跨いでは再現している。**
[Kiyomaru 24](../papers/kiyomaru-2024-comprehensive-analysis.md)・[Ishihara 24](../papers/ishihara-2024-japanese-newspaper.md)・[Takahashi 25b](../papers/takahashi-2025-continual-pretraining-japanese.md) が
日本語で重複の知見を再現しており、[文脈長](context-length.md)のような逆転は報告されていない。

したがって、この Wiki が[ドメインや言語横断](multilingual-and-domain.md)で
整理していた「普遍的要因 vs 文脈依存的要因」という軸は、
**言語軸とデータセット軸で答えが違う**。3 因子のうち
**両方の軸で頑健なのは[モデルサイズ](model-size.md)だけ**である。
→ [対立の台帳](../conflicts.md) 8 番

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

- 重複が効いているのか、**予測の容易さ**が効いているのか。T5 の非単調性は後者を示唆する
- 重複の「単位」はトークンか、文書か、意味的に等価な言い換えを含むか。
  [Tirumala 22] はトークン、[Kandpal 22] は文書で議論しており統一されていない
- 日本語のように語境界が無い言語では、トークナイザ [Kudo 18] の分割方針が
  重複のカウントに影響する可能性がある [Ippolito 23] → [ドメインや言語横断](multilingual-and-domain.md)
- ~~重複回数と暗記量の関数形はドメインによらず一定か~~ → **[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) が否定的に回答。**
  T5 / C4 では単調ですらない。ではどのデータセット特性が関数形を決めるのか
- [Leybzon 24] の暗記・忘却モデルは、バッチサイズや学習率スケジュールを変えても成立するか
