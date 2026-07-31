---
title: 未解決の問い（研究アジェンダ）
type: agenda
---

# 未解決の問い（研究アジェンダ）

23 の概念ページに散在する **105 件**の「未解決の問い」を、
**何が来れば決着するか**で分類して集約したページ。

## 使い方

- **会議 sweep のとき**: 会議のタイトル一覧をこのページと突き合わせる。
  引っかかったものだけ ingest する。「暗記に関する新着論文」を無方向に追わない
- **ingest のとき**: 該当する問いに `→ 論文へのリンク` を追記する。**問いは消さない**
- 各問いの原文と文脈は、リンク先の概念ページにある。ここは索引であって本体ではない

## 決着のさせ方による分類

| 種別 | 件数 | 意味 |
|---|---|---|
| **A. 文献調査で閉じうる** | 約 25 | 既に誰かがやっている可能性が高い。**会議 sweep が直接効く** |
| **B. 実験が要る** | 約 55 | 誰もやっていない。研究テーマの候補 |
| **C. 枠組みの問題** | 約 25 | 定義・目的の設定に依存し、実験では閉じない |

**会議 sweep で動くのは A の約 25 件**である。B は sweep しても
「まだ無い」ことしか分からない（それ自体は価値がある情報だが、頻繁に確認する必要はない）。

---

## 最優先の 10 件

Wiki 全体への波及が大きい順。

| # | 問い | 種別 | 主なページ |
|---|---|---|---|
| 1 | 日本語での[文脈長の逆転](concepts/context-length.md)は、言語特性・定量化手法・評価セット構成のどれに由来するか | B | [文脈長](concepts/context-length.md) [ドメインや言語横断](concepts/multilingual-and-domain.md) |
| 2 | **「メンバーシップ推論が効かなくなった」を抑制手法の成功指標にしてよいか。**抑制手法を測定手法と独立に検証する方法論はどう設計するか | C | [評価の枠組み](concepts/evaluation-framework.md) [逆学習](concepts/machine-unlearning.md) |
| 3 | 日本語・ドメイン特化コーパスで抑制手法（重複排除・PEFT・逆学習）の有効性は再現するか | B | [ドメインや言語横断](concepts/multilingual-and-domain.md) [学習過程における抑制](concepts/mitigation-in-training.md) |
| 4 | 「許容可能な暗記」と「深刻度の高い暗記」を**操作的に**区別する指標は作れるか<br>→ [Carlini 21](papers/carlini-2021-extracting-training-data.md) の k-eidetic が部分的に回答。**なぜ普及しなかったか**が次の問い | C | [暗記](concepts/memorization.md) [評価の枠組み](concepts/evaluation-framework.md) |
| 5 | WikiMIA の分布差問題を踏まえて、過去に報告された手法の優劣は再評価する必要があるか。MIMIR / OLMoMIA での再ランキングは体系的に行われていない | A | [評価セットとライブラリ](concepts/benchmarks-and-tools.md) [メンバーシップ推論](concepts/membership-inference.md) |
| 6 | 「暗記だけ減らして性能を保つ」ことは原理的に可能か。それとも性能とのトレードオフか | B | [暗記と汎化](concepts/memorization-vs-generalization.md) [モデルサイズ](concepts/model-size.md) |
| 7 | 対数線形関係は 6B を大きく超える規模（数百 B〜）でも維持されるか<br>→ [Carlini 23b](papers/carlini-2023-quantifying-memorization.md) の OPT 追試（〜66B）が部分的に回答。傾向は再現するが**効果が数桁小さく**、規模とデータ整理が交絡 | A | [モデルサイズ](concepts/model-size.md) |
| 8 | 異なる定義で測った暗記量を相互に変換・比較する枠組みはあるか | C | [暗記](concepts/memorization.md) [反実仮想](concepts/counterfactual-memorization.md) |
| 9 | 依拠性を立証しうる技術的手段は、メンバーシップ推論以外にあるか | B | [著作権](concepts/copyright.md) |
| 10 | 逆学習は生成を抑えるだけか、パラメータから情報を除去するか | B | [逆学習](concepts/machine-unlearning.md) [知識編集](concepts/knowledge-editing.md) |

---

## A. 文献調査で閉じうる問い（会議 sweep の対象）

**ここが sweep の実質的な検索クエリになる。** 会議のタイトル一覧をこの節と突き合わせる。

### 評価セット・指標

- MIMIR / OLMoMIA 上で、WikiMIA 時代の手法ランキングを再構築した体系的な研究はあるか — [評価セットとライブラリ](concepts/benchmarks-and-tools.md)
- 低偽陽性率領域の指標を採用すると、手法のランキングはどう変わるか — [メンバーシップ推論](concepts/membership-inference.md)
- 目的別の推奨手法を、実際のベンチマークとして具体化した例はあるか — [評価の枠組み](concepts/evaluation-framework.md)
- 評価セット構築時の重複・文脈長バイアスを診断する標準的なチェックリストはあるか — [評価の枠組み](concepts/evaluation-framework.md)
- 日本語の暗記評価に使える標準的なベンチマークはあるか — [ドメインや言語横断](concepts/multilingual-and-domain.md)
- 汚染された状態での性能評価を**補正**する手法はあるか（検出だけでなく） — [データセット汚染](concepts/data-contamination.md)

### スケーリング・学習レシピ

- 対数線形関係は 6B を大きく超える規模でも維持されるか — [モデルサイズ](concepts/model-size.md)
- 混合エキスパート（MoE）では総パラメータ数と活性パラメータ数のどちらが暗記量を規定するか — [モデルサイズ](concepts/model-size.md)
- 「重複排除の効果 = 忘却に任せること」という読み替えは正しいか。学習ステップ数を変えた対照実験があるか — [重複排除](concepts/deduplication.md)
- 継続事前学習で追加コーパスが顕著に暗記される現象は、リプレイで緩和できるか — [学習順と忘却](concepts/training-order-and-forgetting.md)

### 定義・手法の接続

- 剽窃検出の伝統的指標を暗記の定量化に取り込んだ研究は存在するか — [著作権](concepts/copyright.md) [研究領域の拡張](concepts/multimodal-memorization.md)
- **分布シフトのある評価に依拠した既存研究は他にどれだけあるか。**
  [Das 25](papers/das-2025-blind-baselines.md) が名指しした [Panaitescu-Liess 25] は 1 例にすぎない — [評価セットとライブラリ](concepts/benchmarks-and-tools.md)
- 影響関数系の近似は言語モデルの規模でどこまで有効か — [反実仮想](concepts/counterfactual-memorization.md)
- データセット単位の推論は個別著作物の依拠性立証に使えるか — [著作権](concepts/copyright.md)
- 事後学習データの汚染は、事前学習データの汚染と同じ手法で検出できるか — [データセット汚染](concepts/data-contamination.md)
- 多言語モデルにおいて、ある言語の暗記が他言語の出力に転移するか — [ドメインや言語横断](concepts/multilingual-and-domain.md)

### 拡張領域

- マスク型モデルや拡散言語モデルに、自己回帰型の 3 因子はそのまま成立するか — [研究領域の拡張](concepts/multimodal-memorization.md)
- 視覚言語モデルで、画像側とテキスト側の暗記は独立か相互作用するか — [研究領域の拡張](concepts/multimodal-memorization.md)
- 「暗記の局在」はモダリティを超えて共通の構造を持つか — [研究領域の拡張](concepts/multimodal-memorization.md) [知識編集](concepts/knowledge-editing.md)
- 画像で使われる類似度指標は、テキストの意味的類似度と設計上どう対応するか — [研究領域の拡張](concepts/multimodal-memorization.md)

---

## B. 実験が要る問い

誰もやっていない可能性が高い。**研究テーマの候補**であり、sweep で毎回確認する対象ではない。

### 日本語・言語横断（この Wiki 最大のギャップ）

- 日本語での逆転は言語特性・定量化手法・評価セット構成のどれに由来するか — [文脈長](concepts/context-length.md)
- 日本語で文字列類似度ベースの文脈長分析を行うと正の関係が出るか — [文脈長](concepts/context-length.md)
- 語境界の無い他の言語（中国語、タイ語）でも同じ逆転が起きるか — [文脈長](concepts/context-length.md)
- トークナイザを変える（文字単位、バイト単位）と逆転は消えるか — [文脈長](concepts/context-length.md) [ドメインや言語横断](concepts/multilingual-and-domain.md)
- 日本語・ドメイン特化コーパスで抑制手法の有効性は再現するか — [ドメインや言語横断](concepts/multilingual-and-domain.md)
- 日本語のように語境界が無い言語で、トークン一致率や BLEU は妥当な指標か — [文字列の類似度](concepts/string-similarity-memorization.md)
- トークナイザの分割方針が重複のカウントに影響するか — [文字列の重複](concepts/string-duplication.md)
- 日本語など英語以外での知識プローブは何を基準に構築すべきか — [知識を問うタスク](concepts/knowledge-probing.md)

### 「検出されない」と「消えた」の区別

この Wiki で最も繰り返し現れる論点。→ [対立の台帳](conflicts.md)

- 逆学習後のモデルは、反実仮想的な意味で「学習していないモデル」と区別できないか — [逆学習](concepts/machine-unlearning.md)
- 逆学習は生成を抑えるだけか、パラメータから情報を除去するか — [逆学習](concepts/machine-unlearning.md)
- 知識編集で除去した内容は、メンバーシップ推論で検出されなくなるか — [知識編集](concepts/knowledge-editing.md)
- モデル融合は暗記を平均化して薄めるだけか、除去するのか — [知識編集](concepts/knowledge-editing.md)
- 知識蒸留において、教師モデルが暗記した内容は生徒モデルにどの程度伝播するか — [学習過程における抑制](concepts/mitigation-in-training.md)
- 電子透かしの「著作物の生成を抑える」効果と「メンバーシップ推論を妨げる」効果を分離できる設計はあるか — [出力の制御と電子透かし](concepts/output-control-and-watermarking.md)

### 暗記と汎化の分離

- 意味的汎化・構成的汎化は 3 因子とどう関係するか。汎化も対数線形に増えるのか — [暗記と汎化](concepts/memorization-vs-generalization.md)
- 内部表現による暗記と汎化の分離は、逐語的な長文の暗記にも適用できるか — [暗記と汎化](concepts/memorization-vs-generalization.md)
- 「暗記だけ減らして性能を保つ」ことは原理的に可能か — [暗記と汎化](concepts/memorization-vs-generalization.md) [モデルサイズ](concepts/model-size.md)
- 同じ性能で暗記量だけ少ないモデルは原理的に作れるか — [モデルサイズ](concepts/model-size.md)
- 「暗記しても解けないタスク」の設計は本当に可能か — [知識を問うタスク](concepts/knowledge-probing.md)
- 構造分析はモデルサイズを変えても同じ局在を示すか — [知識編集](concepts/knowledge-editing.md)

### メカニズム

- 正則化が暗記を抑制する機序は何か。過学習経由か、別経路か — [学習過程における抑制](concepts/mitigation-in-training.md)
- 忘却の速度は何に依存するか。学習率スケジュール、バッチサイズ、データ順序のどれが支配的か — [学習順と忘却](concepts/training-order-and-forgetting.md)
- 暗記・忘却モデルは、バッチサイズや学習率スケジュールを変えても成立するか — [文字列の重複](concepts/string-duplication.md)
- 逆学習は自然な忘却と同じメカニズムを使えるのか — [学習順と忘却](concepts/training-order-and-forgetting.md)
- PEFT による抑制は学習対象パラメータ数の減少だけで説明できるか — [学習過程における抑制](concepts/mitigation-in-training.md) [モデルサイズ](concepts/model-size.md)
- 中心的仮説（訓練データほど生成確率が大きい）は、重複回数が少ないテキストにも成立するか — [メンバーシップ推論](concepts/membership-inference.md)
- ~~重複回数と暗記量の関数形はドメインによらず一定か~~ → **[Carlini 23b](papers/carlini-2023-quantifying-memorization.md) が否定的に回答**（T5/C4 で非単調）。
  では**どのデータセット特性が関数形を決めるのか** — [文字列の重複](concepts/string-duplication.md)

### 手法の頑健性

- 生成確率へのアクセスを前提としない設定で、既存の実証的知見は再現するか — [メンバーシップ推論](concepts/membership-inference.md)
- 意味的類似度に基づく指標は、逐語暗記で得られた 3 因子の知見をどこまで再現するか — [文字列の類似度](concepts/string-similarity-memorization.md)
- **なぜ重複排除は 100 回超の重複に効かなくなるのか。** 重複排除の不完全性で説明しきれるか — [重複排除](concepts/deduplication.md)
- 重複排除の粒度と暗記抑制効果の関係。近似的な重複を排除すると近似暗記も減るのか — [重複排除](concepts/deduplication.md)
- 重複排除はベンチマーク汚染も減らすか — [重複排除](concepts/deduplication.md) [データセット汚染](concepts/data-contamination.md)
- 近似暗記まで捕捉するフィルタリングは実用的な計算量で可能か — [出力の制御と電子透かし](concepts/output-control-and-watermarking.md)
- 出力フィルタリングを回避する動的プロンプトに対して、後処理はどこまで頑健か — [出力の制御と電子透かし](concepts/output-control-and-watermarking.md)
- 汚染検出が信頼できる最小の粒度は何件か。1 冊の書籍、1 記事まで下げられるか — [データセット汚染](concepts/data-contamination.md)
- 逆学習が他の知識に与える副作用（catastrophic forgetting）の定量化 — [逆学習](concepts/machine-unlearning.md)
- 編集の累積は性能を劣化させるか — [知識編集](concepts/knowledge-editing.md)
- 差分プライバシのパラメータ ε と、実測した暗記量は定量的に対応づけられるか — [差分プライバシ](concepts/differential-privacy.md)
- 「正則化 > DP」という結果は、どの条件下で成立するか — [差分プライバシ](concepts/differential-privacy.md)
- 反実仮想暗記と文字列類似度による暗記はどの程度相関するか。乖離する典型例は何か — [反実仮想](concepts/counterfactual-memorization.md)
- 逆学習の成否を、反実仮想の枠組みで厳密に評価できるか — [反実仮想](concepts/counterfactual-memorization.md)
- データポイズニングの検出は暗記の定量化手法で可能か — [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)
- 「新規性」の指標は、法的な類似性判断とどこまで対応するか — [著作権](concepts/copyright.md)

### 運用・設計

- データ順序を意図的に設計することで暗記を抑制できるか（守りたいデータを学習の前半に置く） — [学習順と忘却](concepts/training-order-and-forgetting.md)
- 削除要求が繰り返し来る運用で、逆学習は累積的に適用できるか — [逆学習](concepts/machine-unlearning.md)
- 外れ値的な機密データを守る手法は何か。重複排除も差分プライバシも効きにくい — [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)
- 「時期で分ける」以外に、訓練セット外のテキストを大量に得る方法はあるか — [評価セットとライブラリ](concepts/benchmarks-and-tools.md)
- 連合学習が主流でない現状で、これらの知見はどこまで外挿できるか — [学習過程における抑制](concepts/mitigation-in-training.md)
- 攻撃速度を評価軸に含めるべき状況はどこか — [評価セットとライブラリ](concepts/benchmarks-and-tools.md)
- 特殊なコーパスを用いた検証は、どこまで一般のモデルに外挿できるか — [評価の枠組み](concepts/evaluation-framework.md)

---

### 原典を読んで分かったこと（2026-07-31）

被参照数の多い 5 本を stub から昇格させた結果、
**サーベイの圧縮で落ちていた知見が問いを 3 つ解消し、2 つ新設した**。

| 問い | 結果 |
|---|---|
| デコーディング戦略の影響に関する対立 | **解消**（比較対象が違った）→ [対立の台帳](conflicts.md) 2 番 |
| 重複回数と暗記量の関数形はドメインによらず一定か | **否定的に回答**（T5/C4 で非単調）→ [対立の台帳](conflicts.md) 8 番 |
| 許容可能な暗記の操作的な区別 | **部分的に回答**（k-eidetic） |
| （新設）なぜ k を持つ定義が普及しなかったのか | 測定可能性が優先された経緯として読める |
| （新設）分布シフトのある評価に依拠した研究は他にどれだけあるか | [Das 25](papers/das-2025-blind-baselines.md) の名指しは 1 例 |

**教訓: 被参照数の多い論文は原典を読む価値がある。**
サーベイは正確だが圧縮されており、圧縮が対立を作ったり留保を落としたりする。

## C. 枠組みの問題（実験では閉じない）

定義や目的の設定に依存する問い。**論文が出ても「決着」はせず、選択肢が増えるだけ**である。
サーベイ 7·1 節の「暗記とは何かを改めて問い直す」に対応する。

- 「許容可能な暗記」と「深刻度の高い暗記」を操作的に区別する指標は作れるか — [暗記](concepts/memorization.md) [評価の枠組み](concepts/evaluation-framework.md) [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)
- 異なる定義で測った暗記量を相互に変換・比較する枠組みはあるか — [暗記](concepts/memorization.md)
- 抑制手法を、測定手法と独立に検証する方法論はどう設計するか — [評価の枠組み](concepts/evaluation-framework.md)
- **「メンバーシップ推論が効かなくなった」を成功指標にしてよいか** — [逆学習](concepts/machine-unlearning.md)
- 暗記と汎化の区別は、許容可能な暗記の区別と同じ問題か、別か。有害な暗記が汎化的に再構成される場合（個人情報の推論）はどちらに属するか — [暗記と汎化](concepts/memorization-vs-generalization.md)
- テキストにおける「1 データ点」の適切な粒度は何か。目的ごとに異なる粒度が要るのか — [差分プライバシ](concepts/differential-privacy.md)
- 公開事前学習コーパスの汚染を前提としたとき、2 段階学習の保証はどう定式化し直せるか — [差分プライバシ](concepts/differential-privacy.md)
- 文脈依存的なプライバシを扱える削除手法は原理的に可能か — [重複排除](concepts/deduplication.md)
- 重複の「単位」はトークンか、文書か、意味的に等価な言い換えを含むか — [文字列の重複](concepts/string-duplication.md)
- 「冒頭の数トークンをプロンプトに」という慣行が、どのドメインでバイアスを生むか — [文字列の類似度](concepts/string-similarity-memorization.md)
- サンプリングによる揺らぎを考慮した場合、決定的な閾値としての「暗記した / していない」は維持できるか — [文字列の類似度](concepts/string-similarity-memorization.md)
- 「訓練後に作成されたデータで評価する」方針が導入する分布差は、汚染の除去と引き換えに何を歪めるか — [データセット汚染](concepts/data-contamination.md) [評価セットとライブラリ](concepts/benchmarks-and-tools.md)
- 事後学習（指示学習・アラインメント）は暗記の測定にどう影響するか — [暗記](concepts/memorization.md)
- 事後学習は知識を問うタスクでの測定結果をどう歪めるか。アラインメントによる拒否は「知らない」と区別できるか — [知識を問うタスク](concepts/knowledge-probing.md) [出力の制御と電子透かし](concepts/output-control-and-watermarking.md)
- マスク型モデルや拡散言語モデルに、自己回帰型で得られた定義はそのまま適用できるか — [暗記](concepts/memorization.md)
- 忘れられる権利への技術的対応は逆学習で十分か。削除の完了をどう検証するか — [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md)
- 法的証明に足る強度を得るには何が必要か — [メンバーシップ推論](concepts/membership-inference.md) [著作権](concepts/copyright.md)
- 日本の著作権法 30 条の 4 第 2 号のもとで、暗記研究のどの成果が実務的に意味を持つか — [著作権](concepts/copyright.md)
- 電子透かしの導入が立証妨害として働く問題に、制度的な対応はありうるか — [著作権](concepts/copyright.md)
- 事実的知識の編集と、長い文字列の逐語暗記の除去は同じ手法で扱えるか — [知識編集](concepts/knowledge-editing.md)
- 3 段階の知識獲得（文字列一致 / 意味的汎化 / 構成的汎化）と 3 因子はどう対応するか — [知識を問うタスク](concepts/knowledge-probing.md)
- 文脈長の概念自体が自己回帰を前提としている。非自己回帰モデルでどう定義し直すか — [研究領域の拡張](concepts/multimodal-memorization.md)
- デコーディング戦略の影響に関する対立は、モデル規模・ドメイン・暗記の定義のどの差から生じるか — [セキュリティと情報漏洩](concepts/security-and-privacy-leakage.md) [対立の台帳](conflicts.md)
