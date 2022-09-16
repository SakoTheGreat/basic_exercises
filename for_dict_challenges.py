# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
povtor9ki = {}
for i in students:
    povtor9ki[i['first_name']] = povtor9ki.get(i['first_name'], 0)+1

for i, j in povtor9ki.items():
    print(f'{i}: {j}')




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
maximalka = {}
for i in students:
    for j, c in i.items():
        maximalka[c] = maximalka.get(c, 0)+1

print(max(maximalka, key=lambda x: maximalka[x]))


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
nu_maksimalka = {}
for spicochek_spiskov in school_students:
    for prost_spisok in spicochek_spiskov:
        for key, ne_pomny in prost_spisok.items():
            nu_maksimalka[ne_pomny] = nu_maksimalka.get(ne_pomny, 0)+1
    print(max(nu_maksimalka, key=lambda x: nu_maksimalka[x]))
    nu_maksimalka = {}

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
dev_o4ko = 0
mal_o4ko = 0
clasiki = ''
for ne_spiski_a_slovari in school:
    clasiki = ne_spiski_a_slovari['class']
    for sosiska_v_spiske in ne_spiski_a_slovari['students']:
        if is_male[sosiska_v_spiske['first_name']]:
            mal_o4ko += 1
        else:
            dev_o4ko += 1
    print(f'Класс {clasiki}: девочки {dev_o4ko}, мальчики {mal_o4ko}')
    dev_o4ko, mal_o4ko, clasiki = 0, 0, ''


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
girls = 0
boys = 0
class_number = ''
all_classes = {}
list_for_all = []
# Ну горит душа просто сделать принт с ответом, но сдерживаюсь=)
for ne_spiski_a_slovari in school:
    class_number = ne_spiski_a_slovari['class']
    for sosiska_v_spiske in ne_spiski_a_slovari['students']:
        if is_male[sosiska_v_spiske['first_name']]:
            boys += 1
        else:
            girls += 1
    all_classes[class_number] = all_classes.get(class_number, [girls, boys])
    girls, boys, class_number, = 0, 0, ''


print(all_classes) 
devochki = sorted(all_classes.items(), key=lambda x: x[1][0], reverse=True)
malchiki = sorted(all_classes.items(), key=lambda x: x[1][1], reverse=True)    

print(f'Больше всего девочек в классе {devochki[0][0]}')
print(f'Больше всего мальчиков в классе {malchiki[0][0]}')