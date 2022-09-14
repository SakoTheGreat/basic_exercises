# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
glasnie_takie_klasnie = 'аеёиоуыэюя'
counter = 0
for i in word.lower():
    if i in glasnie_takie_klasnie:
        counter += 1
print(counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in sentence.split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# Ну как то я странно понимаю это условие, но ладно
dlina = list(map(lambda x: len(x), sentence.split()))
print(sum(dlina)/len(sentence.split()))