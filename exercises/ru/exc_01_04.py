from spacy.lang.en import English

nlp = English()

# Обработка текста
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Перебор токенов документа doc
for token in doc:
    # Проверка на соответствие токена числу
    if ____.____:
        # Получение следующего токена документа
        next_token = ____[____]
        # Проверка на равенство текстового значения следующего токена знаку "%"
        if next_token.____ == "%":
            print("Найдено значение процента:", token.text)
