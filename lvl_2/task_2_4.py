# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
def remove_exclamation_marks(s):
    """
    Функция удаляет все восклицательные знаки из заданной строки.
    :param s: строка для обработки
    :return: строка без восклицательных знаков
    """
    return s.replace('!', '')

# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
def remove_last_em(s):
    """
    Функция удаляет восклицательный знак из конца строки (если есть).
    :param s: строка для обработки
    :return: строка без восклицательного знака в конце
    """
    if s.endswith('!'):
        return s.rstrip('!')
    else:
        return s

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
def remove_word_with_one_em(s):
    """
    Функция удаляет слова из предложения, если они содержат ровно один восклицательный знак.
    :param s: строка для обработки
    :return: строка без слов, содержащих ровно один восклицательный знак
    """
    words = s.split()
    new_words = []
    for word in words:
        if word.count('!') != 1:
            new_words.append(word)
    return ' '.join(new_words)


# Пример использования:

s1 = "Hi! Hello!"
s2 = ""
s3 = "Oh, no!!!"
s4 = "Hi!"
s5 = "Hi!!!"
s6 = "!Hi"
s7 = "Hi! Hi!"
s8 = "Hi! Hi! Hi!"
s9 = "Hi Hi! Hi!"
s10 = "Hi! !Hi Hi!"
s11 = "Hi! Hi!! Hi!"
s12 = "Hi! !Hi! Hi!"

# Пункт A
print(remove_exclamation_marks(s1))  # Hi Hello
print(remove_exclamation_marks(s2))  #
print(remove_exclamation_marks(s3))  # Oh, no

# Пункт B
print(remove_last_em(s4))  # Hi
print(remove_last_em(s5))  # Hi!!
print(remove_last_em(s6))  # !Hi

# Пункт C
print(remove_word_with_one_em(s1))  #
print(remove_word_with_one_em(s7))  # Hi
print(remove_word_with_one_em(s8))  #
print(remove_word_with_one_em(s9))  # Hi
print(remove_word_with_one_em(s10))  #
print(remove_word_with_one_em(s11))  # Hi!!
print(remove_word_with_one_em(s12))  # !Hi!
