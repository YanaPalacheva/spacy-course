---
type: slides
---

# モデルとルールの組み合わせ

Notes: 機械学習モデルとルールベースシステムの組み合わせは、NLPツールにあるべき最も強力な機能の一つです。

このレッスンでは、spaCyでそれを行う方法をみていきます。

---

# 機械学習モデルの予測 vs. ルール

|                         | **機械学習モデル**                                      | **ルールベースシステム**            |
| ----------------------- | ----------------------------------------------------------- | --------------------------------- |
| **使用場面**             | 例をもとに汎化する必要があるアプリケーション | |
| **実際の例**             | 製品、人物の名前、主語/目的語の関係性 |                                   |
| **spaCyの機能**      | 固有表現抽出、依存関係解析、品詞タグづけ |                                   |

Notes: 機械学習モデルは、アプリケーションがいくつかの例に基づいて一般化する必要がある場合に便利です。

例えば、製品名や人名の検出に役立ちます。大量の人名のデータを用意する代わりに、あるスパンが人名を表すかどうかを予測できるようにすることができます。
同様に、依存関係ラベルを予測することで主語目的語の関係を探すことができます。

これらを行うために、spaCyの固有表現抽出器、依存関係解析器、品詞タグづけ機能を使いましょう。

---

# 機械学習モデルの予測 vs. ルール

|                         | **機械学習モデル**                                      | **ルールベースシステム**            |
| ----------------------- | ----------------------------------------------------------- | --------------------------------- |
| **使用場面**             | 例をもとに汎化する必要があるアプリケーション | 有限の辞書データ |
| **実際の例**             | 製品、人物の名前、主語/目的語の関係性 | 国名、町名、薬名、犬の種類       |
| **spaCyの機能**      | 固有表現抽出、依存関係解析、品詞タグづけ | トークナイザ、 `Matcher`、 `PhraseMatcher`   |

Notes: 一方、ルールベースのアプローチは、見つけたい実体の数が多かれ少なかれ限られている場合に便利です。例えば、世界のすべての国や都市、薬の名前、犬の品種などです。

spaCyでは、カスタムのトークン化ルールやmatcher、phrase matcherで実現できます。

---

# 要約：ルールベースマッチ

```python
# 共有語彙データで初期化
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)

# パターンはトークンを表す辞書のリストからなります
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", None, pattern)

# 演算子は何回トークンがマッチするかを表します
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", None, pattern)

# matcherをdocに対して呼び出し、(match_id, start, end)のリストを取得
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)
```

Notes: 前章で、spaCyのルールベースのmatcherを使って複雑なパターンを文章中から見つける方法を学びました。
ここでは、その簡単な要約を掲載しています。

matcherは共有語彙データ（通常は`nlp.vocab`）によって初期化されます。

パターンは辞書のリストです。辞書はそれぞれのトークンとその属性について記述します。
パターンは`matcher.add`メソッドを用いてmatcherに追加します。

演算子によって、どの程度トークンにマッチするかを指定できます。
例えば、「+」は1回以上マッチします。

matcherをdocオブジェクトに対して呼び出すと、マッチ結果のリストが帰ってきます。
それぞれのマッチ結果は、IDとdocの開始インデックスと終了インデックスを要素とするタプルからなります。

---

# 機械学習の予測を加える

```python
matcher = Matcher(nlp.vocab)
matcher.add("DOG", None, [{"LOWER": "golden"}, {"LOWER": "retriever"}])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # スパンのルートのトークンと、そのヘッドトークンを取得
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # 以前のトークンとその品詞タグを出力
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)
```

```out
Matched span: Golden Retriever
Root token: Retriever
Root head token: have
Previous token: a DET
```

Notes: これは「golden retriever」のルールの例です。

マッチ結果をイテレートすると、マッチIDと、マッチしたスパンの開始インデックスと終了インデックスを取得でき、より詳細な情報を見ることができます。
`Span` オブジェクトを用いると、元の文書やその他のすべてのトークン属性、モデルによって予測された特徴量にアクセスすることができます。

例えば、スパンのルートトークンを取得することができます。スパンが複数のトークンで構成されている場合、これはフレーズのカテゴリを決定するトークンになります。
例えば、「ゴールデンレトリバー」のルートは「レトリバー」です。また、このルートのヘッドトークンを取得できます。
これはフレーズを支配する構文的な「親」であり、この場合は動詞「have」です。

最後に、前のトークンとその属性をみていきます。この場合は限定詞「a」です。

---

# 効率的なフレーズマッチング(1)

- `PhraseMatcher`は正規表現やキーワードサーチのようなものですが、トークンベースです
- `Doc`オブジェクトをパターンとして使います
- `Matcher`より速く、効率的です
- 大量の単語リストのマッチに用いると強力です

Notes: phrase matcherは、データから単語列を探すための便利なツールです。

doc中のキーワードを探しますが、文字列ではなくトークンを探すので、文脈情報に直接アクアスできます。

`Doc`オブジェクトをパターンとして取ります。

そして、とても高速です。

なので、大きな辞書や単語リストをもとに、大量のテキストに対してマッチングを行う際はとても便利です。

---

# 効率的なフレーズマッチ(2)

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add("DOG", None, pattern)
doc = nlp("I have a Golden Retriever")

# マッチの結果をイテレート
for match_id, start, end in matcher(doc):
    # マッチ結果のスパンを取得
    span = doc[start:end]
    print("Matched span:", span.text)
```

```out
Matched span: Golden Retriever
```

Notes: 例をみていきます。

phrase matcherは`spacy.matcher`からインポートします。そして、普通のmatcherと同じAPIを持ちます。

辞書のリストを渡す代わりに、`Doc`をパターンとして渡します。

そして、テキスト中のマッチ結果をイテレートし、マッチIDと開始インデックス、終了インデックスを取得します。
これによって、マッチした「Golden Retriever」の`Span`オブジェクトを作ることができ、文脈を解析できます。

---

# Let's practice!

Notes: それでは、ルールと機械学習モデルを組み合わせるために新しく学んだテクニックを実践していきましょう。
