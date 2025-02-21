---
type: slides
---

# 処理パイプライン

Notes: Welcome back！
この章では処理パイプラインを紹介します。
処理パイプラインとは、docに品詞タグや依存関係ラベル、固有表現を追加する一連の関数です。

このレッスンでは、spaCyが提供しているパイプラインコンポーネントを見ていき、文字列に対してnlpオブジェクトを呼び出したときに裏側で起こることを学びます。

---

# nlpを呼び出すと何が起こる？

<img src="/pipeline.png" alt="spaCyパイプラインが文字列をDocに変換する図解" width="90%" />

```python
doc = nlp("This is a sentence.")
```

Notes:

`nlp` オブジェクトにテキストの文字列を渡し、`Doc` オブジェクトを受け取るコードを何度も書いてきました。

しかし、`nlp` オブジェクトは実際に何をしているのでしょうか？

まず、トークナイザーを適用してテキストの文字列を `Doc` オブジェクトに変換します。次に、一連のパイプラインコンポーネントが順にDocに適用されます。この場合、タグ付け器、パーサ、固有表現器の順に適用されます。最後に、処理されたdocが返されます。

---

# ビルトインのパイプラインコンポーネント

| Name        | Description             | Creates                                                   |
| ----------- | :---------------------- | :-------------------------------------------------------- |
| **tagger**  | 品詞タグ付け   | `Token.tag`, `Token.pos`                                  |
| **parser**  | 依存関係解析 | `Token.dep`, `Token.head`, `Doc.sents`, `Doc.noun_chunks` |
| **ner**     | 固有表現器 | `Doc.ents`, `Token.ent_iob`, `Token.ent_type`             |
| **textcat** | 文書分類 | `Doc.cats`                                                |

Notes:
spaCyには以下のパイプラインコンポーネントが同梱されています。

品詞タグづけ器は `token.tag` と `token.pos` 属性を設定します。

依存関係解析器は `token.dep` と `token.head` 属性を追加し、文や基本名詞句を検出します。

固有表現抽出器は、抽出された固有表現を `doc.ents` プロパティに追加します。また、トークンに固有表現タイプ属性を設定し、トークンが固有表現の一部であるかどうかを示します。

最後に、文書分類器は、テキスト全体に適用されるカテゴリラベルを設定し、`doc.cats` プロパティに追加します。

テキストのカテゴリは特殊なものなので、文書分類器はデフォルトではどの事前学習モデルにも含まれていません。しかし、これを使って独自のシステムを学習することができます。

---

# 舞台裏

<img src="/package_meta.png" alt="en_core_web_smのフォルダ、ファイル、meta.jsonの図解" />

- モデルの `meta.json` で定義されているパイプラインを順番に並べます
- コンポーネントは、予測を行うために重みを必要とします

Note: spaCyがロードできるすべてのモデルには、いくつかのファイルと `meta.json` が含まれています。

meta.jsonは言語やパイプライン等を定義しており、インスタンス化するコンポーネントをspaCyに伝えます。

予測を行うコンポーネントには重みデータも必要です。データはモデルパッケージに含まれており、モデルをロードする際にコンポーネントにロードされます。

---

# Pipeline attributes

- `nlp.pipe_names`: コンポーネントの名前のリスト

```python
print(nlp.pipe_names)
```

```out
['tagger', 'parser', 'ner']
```

- `nlp.pipeline`: `(name, component)`のタプルのリスト

```python
print(nlp.pipeline)
```

```out
[('tagger', <spacy.pipeline.Tagger>),
 ('parser', <spacy.pipeline.DependencyParser>),
 ('ner', <spacy.pipeline.EntityRecognizer>)]
```

Notes: 現在のnlpオブジェクトに含まれるパイプラインコンポーネントの名前を見るには、`nlp.pipe_names`属性を利用します。

コンポーネント名とコンポーネント関数のタプルの一覧を見るには `nlp.pipeline` 属性を用います。

コンポーネント関数は、docを処理したり属性を設定したりするためにdocに適用される関数です。

---

# Let's practice!

Notes: spaCyのパイプラインをいくつかチェックし、舞台裏を覗いてみましょう！
