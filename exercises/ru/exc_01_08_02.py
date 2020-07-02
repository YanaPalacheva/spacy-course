import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Обработка текста
doc = ____

# Перебор всех предсказанных именованных сущностей
for ent in ____.____:
    # Вывод текстового значения сущности и её аннотации
    print(ent.____, ____.____)
