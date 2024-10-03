def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words


result1 = single_root_words('дом', "домашний","беЗДомнЫЙ","Хата","мода","Дима")
result2 = single_root_words('крот', "кроТовый", "корОТкий","кРАтко","Кэрот")
print(result1)
print(result2)


