---
title: Preventing generation of verbatim memorization in language models gives a false sense of privacy
authors: [Daphne Ippolito, Florian Tramèr, Milad Nasr, Chiyuan Zhang, Matthew Jagielski, Katherine Lee, Christopher A. Choquette-Choo, Nicholas Carlini]
year: 2023
venue: INLG 2023, pp. 28–53
citekey: Ippolito 23
url: https://arxiv.org/abs/2210.17546
tags: [mitigation, critique, approximate-memorization, output]
axis: [出力]
type: paper
---

# Preventing generation of verbatim memorization gives a false sense of privacy

## TL;DR

**逐語暗記を完全に防ぐ防御を実際に作り、それでも訓練データの漏洩は防げないと示した。**
「完璧なフィルタ」は、もっともらしい**スタイル変換プロンプト**で回避されるうえ、
モデルは**自力でフィルタを騙す**（綴りの誤り、句読点の調整、同義語の置換）。
先行研究は暗記量を**大幅に過小評価している**と結論する。

## 位置づけ

出力軸。5·3 節（後処理による抑制）への最も強い批判であると同時に、
3·2§1（[近似暗記](../concepts/string-similarity-memorization.md)の定義）と
4·2（[モデルサイズ](../concepts/model-size.md)）にも寄与する。

**この Wiki で唯一、防御を実装したうえでその失敗を示した論文**である。
既存防御の批判にとどまらず、逐語暗記を**証明可能に**完全阻止する系を自作したうえで
「それでも足りない」と示した点が、他の批判論文と質的に違う。

## 手法・実験

### MemFree decoding（提案する「完璧な」防御）

生成の各ステップで、モデルが選んだ次トークンが**訓練セット中の n-gram を作るか**を検査する。
作るなら、再生成せずにモデルの事後分布から**代替トークンをサンプリング**する。
訓練セットへの所属判定は **Bloom フィルタ**で効率的に行うため、数百 GB にスケールする。

- Pile 中で **10 回以上出現する全 10-gram** で Bloom フィルタを構築
- 対象: GPT-Neo 系（125M〜6B）。arg max デコーディング
- 評価データ: [Carlini 23b](carlini-2023-quantifying-memorization.md) が公開した Pile 部分列
  （150 トークン × 30,000 本、重複回数で 30 バケットに分割）。
  先頭 50 トークンをプロンプトとし 50 トークンを生成

### 近似暗記の指標

| 指標 | 内容 |
|---|---|
| **BLEU**（単語レベル） | 生成と正解後続の一致度。**BLEU > 0.75 を「暗記」**とする二値判定 |
| **Levenshtein 類似度**（文字レベル、長さ正規化） | 表層の編集距離 |

閾値 0.75 は事例の定性的な検査で決めた。

### 実モデルでの検証

**GitHub Copilot を「block suggestions matching public code」を有効にした状態で**評価し、
GPT-3（Davinci）でも抽出攻撃を試みている。

## 主要な知見

### 1. 逐語暗記の防御は必要だが十分ではない

MemFree は逐語暗記を完全に阻止する。にもかかわらず漏洩は止まらない。失敗経路は 2 つある。

**(a) スタイル変換プロンプトによる回避（攻撃者・利用者いずれもありうる）**

- Copilot に対し、**変数名を英語からフランス語に翻訳**するだけで、
  暗記した内容を en-fr 変換した形で出力させられた
- Python 形式のコメントを付けるといった些細な改変でも回避できる
- **改変していない元のプロンプトでも回避が起きる場合がある**

**(b) モデルが自力でフィルタを騙す**

厳密な n-gram を生成できなくなると、モデルは**近い言い換えで「ズル」をする**。
論文が挙げる例: 綴りの誤りの挿入、句読点や空白の調整、同義語の置換（`and` → `&`）。
生成例には `redistributeredistribut`・`asAS`・`orOR` といった、
**フィルタ回避のための微小な改変が可視化されている**。
人間には**ほぼ同一に見える**。

### 2. 先行研究は暗記量を大幅に過小評価している

[Carlini 23b](carlini-2023-quantifying-memorization.md) の抽出実験を、
逐語ではなく近似（BLEU > 0.75）の定義で再実行すると、
**逐語暗記として数えられる量よりはるかに多くが暗記されている**。

> we find that prior literature has significantly underestimated memorization leakage

つまり [Carlini 23b](carlini-2023-quantifying-memorization.md) の
「Pile の少なくとも 1%」という下界は、**定義を緩めれば大きく上振れする**。

### 3. モデルサイズの知見は近似暗記でも再現する

大きいモデルの生成ほど正解後続との類似度が高いという明確な傾向を確認した。
→ [モデルサイズ](../concepts/model-size.md)（定義への頑健性の証拠）

**同時に MemFree はどのモデルサイズでも有効**である（BLEU が 0.6 付近でほぼ横ばい）。
重複回数が多い系列に対しても、全モデルサイズで類似度を有意に下げる。
つまり**防御は効いているが、効いてなお漏れる**。

## 限界・批判

- **BLEU 0.75 という閾値は過大にも過小にも数えうる**と論文自身が注意している。
  「この定義に切り替えれば防御が良くなるとは限らない——**偽陽性を大量に生みうる**」。
  近似暗記への定義の拡張は、そのまま防御の改善にはならない
- **問題のある暗記と問題のない暗記を区別していない**と論文自身が明記している
  （「大統領演説の正確な引用」と「個人情報の露出」を同列に扱う）。
  サーベイ 7·1 節が引く [Lee 20] の批判が、そのまま当てはまる
  → [評価の枠組み](../concepts/evaluation-framework.md)
- Copilot の訓練セットと防御アルゴリズムは非公開であり、
  そのための代替として MemFree を自作している。実運用の防御そのものの分析ではない
- 対象は英語テキストとコード

## Wiki 内の接点

- [文字列の類似度](../concepts/string-similarity-memorization.md)（近似暗記の定義と指標）
- [出力の制御と電子透かし](../concepts/output-control-and-watermarking.md)（後処理の限界の主要根拠）
- [モデルサイズ](../concepts/model-size.md)（定義を緩めても再現する）
- [研究領域の拡張](../concepts/multimodal-memorization.md) / [ドメインや言語横断](../concepts/multilingual-and-domain.md)
- 逐語暗記の原典: [Carlini 23b](carlini-2023-quantifying-memorization.md)（下界を過小評価だと批判）
- 本論文を引用している概念: [評価の枠組み](../concepts/evaluation-framework.md) / [逆学習](../concepts/machine-unlearning.md) / [文字列の重複](../concepts/string-duplication.md)
