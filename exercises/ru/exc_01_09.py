import spacy

nlp = spacy.load("en_core_web_sm")

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Обработка текста
doc = ____

# Перебор именованных сущностей
for ____ in ____.____:
    # Вывод текстого значения и аннотации текущей именованной сущности
    print(____.____, ____.____)

# Получение спана для "iPhone X"
iphone_x = ____

# Вывод текстового значения спана
print("Missing entity:", iphone_x.text)
