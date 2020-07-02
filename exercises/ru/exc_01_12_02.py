import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# Шаблон, которому соответствует любая форма "download" + имя собственное
pattern = [{"LEMMA": ____}, {"POS": ____}]

# Добавление шаблона в матчер и применение матчера к документу
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# Перебор найденных соответствий и вывод их текстовых значений
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
