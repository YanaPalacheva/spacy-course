import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Features of the app include a beautiful design, smart search, automatic "
    "labels and optional voice responses."
)

# Шаблон для последовательности прилагательное + существительное (одно или два)
pattern = [{"POS": ____}, {"POS": ____}, {"POS": ____, "OP": ____}]

# Добавление шаблона в матчер и применение матчера к документу
matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# Перебор найденных соответствий и вывод их текстовых значений
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
