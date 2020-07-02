# Импорт класса английского языка и создание объекта nlp
from ____ import ____

nlp = ____

# Обработка текста
doc = ____("I like tree kangaroos and narwhals.")

# Срез объекта Doc, соответствующий токенам "tree kangaroos"
tree_kangaroos = ____
print(tree_kangaroos.text)

# Срез объекта Doc, соответствующий токенам "tree kangaroos and narwhals" (без ".")
tree_kangaroos_and_narwhals = ____
print(tree_kangaroos_and_narwhals.text)
