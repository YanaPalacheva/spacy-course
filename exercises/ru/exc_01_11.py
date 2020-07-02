import spacy

# Импорт класса Matcher
from spacy.____ import ____

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Инициализация матчера с общим вокабуляром в виде аргумента
matcher = ____(____.____)

# Создание шаблона для двух токенов: "iPhone" and "X"
pattern = [____]

# Добавление шаблона в матчер
____.____("IPHONE_X_PATTERN", None, ____)

# Применение матчера к документу
matches = ____
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
