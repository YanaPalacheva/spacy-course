import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Обработка текста
doc = ____

for token in doc:
    # Получение значения текста, части речи и синтаксической роли текущего токена
    token_text = ____.____
    token_pos = ____.____
    token_dep = ____.____
    # Строка для форматирования вывода
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
