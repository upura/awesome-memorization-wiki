---
title: 逆学習（Machine Unlearning）
aliases: [machine unlearning, 逆学習, アンラーニング, 忘却学習]
axis: モデル
survey_section: "5·2"
tags: [mitigation, model]
type: concept
---

# 逆学習（Machine Unlearning）

## 定義

特定の訓練データに対して、学習済みのモデルを**通常とは逆方向の勾配**に
ファインチューニングする手法（[Ishihara 26](../papers/ishihara-2026-memorization-survey.md) 5·2、
[Bourtoule 21], [Liu 25]）。特定の訓練データに関する生成が発生しづらくなる効果が期待できる。
強化学習を用いる研究もある [Kassem 23]。

## 主要な論文

- [Bourtoule 21] — Machine unlearning（IEEE S&P 2021）。逆学習の枠組み
- [Liu 25] — 大規模言語モデルにおける逆学習の再考（Nature Machine Intelligence）
- [Kassem 23] — Dememorization。強化学習を用いた暗記リスクの緩和
- [Tran 25] — トークン単位での学習・忘却の二重目的訓練。メンバーシップ推論への防御にも寄与

## 横断的知見

**逆学習の理想は [反実仮想](counterfactual-memorization.md)そのものである。**
「そのデータが最初から無かった状態のモデル」に戻すことが目標なのだから、
**逆学習の成否をどう測るかという問題は、反実仮想暗記をどう測るかという問題に還元される**。
そして反実仮想暗記の測定は多数のモデルを学習する必要があり計算コストが高い
（[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) の指摘）。
逆学習の評価が難しいことと、反実仮想的定義が使われないことは同じ根を持つ（推測）。

**「削除できない」ことへの事後的な回答という位置づけ。**
[前処理によるデータの削除](deduplication.md)は、プライバシの文脈依存性
[Dourish 04, Nissenbaum 09] のため文字列だけからは判定できず限界がある
（[Brown 22](../papers/brown-2022-what-does-it-mean-privacy.md)）。
逆学習は「学習後に削除要求が来る」現実——[忘れられる権利](security-and-privacy-leakage.md)や
GDPR——に対応する唯一の手段である。
つまり抑制手法の 3 段階のうち、**唯一「事後に発生した要求」に応えられる層**である。

**[自然な忘却](training-order-and-forgetting.md)との関係が未整理である。**
学習中には暗記と忘却が並行して発生している [Duan 24]。
一度しか出現しない文字列は「忘却され続ける」[Leybzon 24]。
逆学習が誘導する忘却が、この自然な忘却と同じ機構を使っているのか、
それとも表層的に生成を抑えているだけなのかは、この Wiki では区別できていない。
後者なら [出力の制御](output-control-and-watermarking.md)に近く、
[Ippolito 23](../papers/ippolito-2023-false-sense-of-privacy.md) の「偽りの安心感」批判が同様に当てはまる可能性がある。

**メンバーシップ推論への防御としても機能する。** [Tran 25] は
トークンの絞り込みがメンバーシップ推論に対する防御に役立つと報告した。
ただし [電子透かし](output-control-and-watermarking.md)でも同様に
メンバーシップ推論の成功確率が低下することが観測されており
[Panaitescu-Liess 25]、**「メンバーシップ推論が効かなくなること」は
暗記が消えたことの証拠にならない**。防御と測定不能化の区別が要る。

## 未解決の問い

- 逆学習後のモデルは、反実仮想的な意味で「そのデータを学習していないモデル」と
  区別できないか。区別できるなら何が残っているか
- 逆学習は生成を抑えるだけか、パラメータから情報を除去するか。
  [知識編集](knowledge-editing.md) の分析手法 [Menta 25] で切り分けられるか
- 逆学習が他の知識に与える副作用（catastrophic forgetting）の定量化
- **「メンバーシップ推論が効かなくなった」を成功指標にしてよいか。**
  [Panaitescu-Liess 25] と [Tran 25] を並べると、この指標の妥当性は疑わしい
- 削除要求が繰り返し来る運用（GDPR 対応）で、逆学習は累積的に適用できるか
