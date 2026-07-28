---
title: 「メンバーシップ推論が効かなくなった」を抑制手法の成功指標にしてよいか
date: 2026-07-29
type: query
tags: [methodology, mitigation, evaluation]
---

# Q. 「メンバーシップ推論が効かなくなった」を抑制手法の成功指標にしてよいか

## A. よくない。3 つの独立した経路が同じ落とし穴を示している

[メンバーシップ推論](../concepts/membership-inference.md) の成功率低下は、次の 3 つのいずれとも整合する。
指標としては**識別力が無い**。

- 暗記そのものが減った（望ましい）
- 防御が成功した（望ましいが、暗記は残っている）
- **測定が不能になっただけ**（望ましくない）

### 根拠

| 経路 | 報告 | 出典 |
|---|---|---|
| [電子透かし](../concepts/output-control-and-watermarking.md) | 著作物の生成確率が格段に小さくなる一方、**メンバーシップ推論の成功確率も低下する** | [Panaitescu-Liess 25] |
| [逆学習](../concepts/machine-unlearning.md) | 利用するトークンの絞り込みがメンバーシップ推論への防御に役立つ | [Tran 25] |
| [逆学習](../concepts/machine-unlearning.md) | 生成を抑えているのかパラメータから情報を除去したのか、この Wiki では区別できない | — |

## なぜこの問いをファイリングしたか

この結論は [Ishihara 26](../papers/ishihara-2026-memorization-survey.md) のどの節にも明示されていない。
5·3 節（電子透かし）、5·2 節（逆学習）、7·1 節（評価の枠組み）に分散した記述を
突き合わせて初めて立つ。**Wiki を作ったことで見えた繋がり**である。

[評価の枠組み](../concepts/evaluation-framework.md) の `## 横断的知見` に還元済み。

## より深い含意：著作権

[Panaitescu-Liess 25] の結果は、権利者にとって不利に働く。
サーベイ 6·2 節によれば、著作権侵害の**依拠性**は [メンバーシップ推論](../concepts/membership-inference.md) に対応する。
つまりモデル提供者が電子透かしを導入すると、
著作物の生成（類似性）を抑えると同時に、
**「あなたのデータで学習した」ことの立証（依拠性）も困難になる**。

[Zhang 25a](../papers/zhang-2025-mia-cannot-prove.md) の「証明にならない」という立場と、
[Das 25](../papers/das-2025-blind-baselines.md) の評価セット批判を合わせると、
依拠性の立証経路は**方法論・防御策の両側から狭められている**。
→ [著作権](../concepts/copyright.md) の `## 横断的知見` に還元済み。

## では何を成功指標にすべきか

Wiki は明確な答えを持たない。**知識ギャップ**として [評価の枠組み](../concepts/evaluation-framework.md) の
`## 未解決の問い` に登録した。方向性として言えるのは:

- 抑制手法の評価には、**抑制対象の測定手法とは独立の検証**が要る
- [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) は原理的にはこの独立性を持つが、
  多数のモデルを学習する必要があり計算コストが高い
  （[Carlini 23b](../papers/carlini-2023-quantifying-memorization.md) の指摘）。
  **理論的に正しい指標が使えないことが、この問題の根にある**

## Wiki 内の接点

[評価の枠組み](../concepts/evaluation-framework.md) / [逆学習](../concepts/machine-unlearning.md) / [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md) /
[著作権](../concepts/copyright.md) / [反実仮想に基づく定義](../concepts/counterfactual-memorization.md) / [メンバーシップ推論](../concepts/membership-inference.md)
