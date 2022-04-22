# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
# (Football Coach)
#  Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
#  Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите
# методом strip знаки препинания)
#  Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
# Усложнённое ** (можно сначала его не делать):
#  Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество
# «встречаний» этого слова)
#  Слова с большой буквы и с маленькой это все равно одно и тоже слово

phrase = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)"""
print(phrase)
words_list = phrase.split()


print(words_list)
print("The phrase has", len(words_list), "words")
print("******************************************************************\n")


for i in range(len(words_list)):
    punct = ['!', ',', '.', '(', ')', ':', ';', '?', '-']
    for sign in punct:
        words_list[i] = words_list[i].strip(sign)
print(words_list)
print("******************************************************************\n")


sort_words = words_list
sort_words.sort()
print(sort_words)
print("******************************************************************\n")


word_dict = dict.fromkeys(words_list, 0)
for word in words_list:
    if word_dict.get(word) == 0:
        word_dict.update({word: words_list.count(word)})
print(word_dict)
print("******************************************************************\n")


for i in range(len(words_list)):
    words_list[i] = words_list[i].lower()
print(words_list)
word_dict = dict.fromkeys(words_list, 0)
for word in words_list:
    if word_dict.get(word) == 0:
        word_dict.update({word: words_list.count(word)})
print(word_dict)