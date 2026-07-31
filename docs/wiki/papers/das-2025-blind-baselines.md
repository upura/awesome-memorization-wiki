---
title: Blind baselines beat membership inference attacks for foundation models
authors: [Debeshee Das, Jie Zhang, Florian Tramèr]
year: 2025
venue: "IEEE Security and Privacy Workshops (SPW) 2025, pp. 118–125（2nd DATA-FM workshop @ ICLR 2025 版あり）"
citekey: Das 25
url: https://arxiv.org/abs/2406.16201
tags: [membership-inference, critique, benchmark]
axis: [出力]
type: paper
---

# Blind baselines beat membership inference attacks for foundation models

## TL;DR

**モデルを一切見ない「盲目的」攻撃が、8 つの公開評価データセットすべてで
最先端のメンバーシップ推論手法を上回った。**
既存の評価は正例と非正例を**異なる分布から抽出**しており、
「現行の評価は基盤モデルの訓練データの漏洩について何も語っていない」と結論する。

## 位置づけ

出力軸。[メンバーシップ推論](../concepts/membership-inference.md)の方法論に対する
最も直接的な反証であり、サーベイ 3·2§2 の評価セット批判の中核。

サーベイは WikiMIA の時期的な分布差を指摘するにとどまるが、
原論文の主張は**はるかに広い**——時期的シフトは特殊例の一つにすぎず、
テキスト・画像を通じた 8 データセットで有意な分布シフトを同定している。

## 手法・実験

### 盲目的（blind）攻撃

**対象モデルを完全に無視して**正例と非正例を判別する。手法は素朴である。

- 時期的シフトのあるデータセット: 各サンプルから抽出した**日付に閾値**をかける
- その他のテキスト / テキスト画像データセット:
  キャプションに対する単純な **bag-of-words または n-gram 分類器**

### 結果（論文 Table 1）

| 評価データセット | 指標 | 既存手法の最良値 | 盲目的攻撃 |
|---|---|---|---|
| WikiMIA | TPR@5%FPR | 43.2% | **94.7%** |
| BookMIA | AUC ROC | 88.0% | **91.4%** |
| Temporal Wiki | AUC ROC | 79.6% | **79.9%** |
| Temporal ArXiv | AUC ROC | 74.5% | **75.3%** |
| ArXiv (all vs 1 month) | TPR@1%FPR | 5.9% | **10.6%** |
| ArXiv (1 month vs 1 month) | TPR@1%FPR | 2.5% | **2.7%** |
| LAION-MI | TPR@1%FPR | 2.5% | **8.9%** |
| Gutenberg | TPR@1%FPR | 18.8% | **55.1%** |

**8 つすべてで盲目的攻撃が上回る。**

## 主要な知見

### 1. 問題は WikiMIA と時期的シフトに限らない

サーベイの記述は WikiMIA の年号に集約されているが、原論文は
**テキストと画像にまたがる 8 データセットで、時期以外の分布シフトも同定**している。
LAION-MI（画像・テキスト）や Gutenberg（書籍）も含む。
つまりこれは 1 つのデータセットの設計ミスではなく、
**評価セットを事後的に構成するという方法そのものの欠陥**である。

### 2. 事後的なバイアス除去は脆い

> such simple methods work even for MI evaluation datasets that were
> **explicitly designed to remove distribution shifts** between members and non-members.
> Our work shows that removing biases in a post-hoc fashion is highly brittle.

分布シフトを取り除くように設計されたデータセットでも、素朴な分類器が通る。
**「バイアスを除いた」という主張自体が検証困難**である。

### 3. これらの評価に依拠した研究も信頼できない

論文は具体的に **[Panaitescu-Liess 25]（電子透かしがメンバーシップ推論に与える影響）**を
名指しし、明確な分布シフトのあるデータセットで評価しているため信頼できないと述べる。
→ この Wiki への影響は
[出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)と
[評価の枠組み](../concepts/evaluation-framework.md)を参照。

### 4. 推奨される評価方法

**明確な train-test 分割を持つモデルで評価すべき**である。
具体例として Pile [Gao 20]、DataComp、DataComp-LM のランダム部分集合を挙げている。
つまり事後的に非正例を作るのではなく、**最初から分割を設計する**。
→ [対立の台帳](../conflicts.md) 3 番（「時期で分ける」設計）に対する回答でもある。

## 限界・批判

- 「既存の評価が壊れている」ことは示すが、**正しい手法のランキングは与えない**。
  MIMIR [Duan 24](duan-2024-do-mia-work.md) や OLMoMIA [Kim 26] 上での
  体系的な再ランキングは、この Wiki では未確認
- 盲目的攻撃が上回ることは、既存手法が**漏洩を全く捉えていない**ことの証明ではない。
  論文自身の言い方は「データ特徴に基づいて（まずい形で）推論している可能性を排除できない」であり、
  漏洩がゼロだと主張しているわけではない
- ワークショップ論文であり、分量は限られる

## Wiki 内の接点

- [評価セットとライブラリ](../concepts/benchmarks-and-tools.md) / [メンバーシップ推論](../concepts/membership-inference.md) / [評価の枠組み](../concepts/evaluation-framework.md)
- 批判対象: [Shi 24](shi-2024-min-k-prob.md)（WikiMIA）
- 同方向: [Chen 25](chen-2025-revisiting-mia.md) / [Duan 24](duan-2024-do-mia-work.md) / [Zhang 25a](zhang-2025-mia-cannot-prove.md)（共著者が重なる）
- 著作権立証への含意: [著作権](../concepts/copyright.md)
- 本論文を引用している概念: [データセット汚染](../concepts/data-contamination.md) / [文脈長](../concepts/context-length.md) / [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)
