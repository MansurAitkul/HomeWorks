def caesar_cipher(shift, text):
    result = ''
    for char in text:
        if char.isalpha():
            base = 'a' if char.islower() else 'A'
            offset = (ord(char) - ord(base) + shift) % 26
            result += chr(ord(base) + offset)
        else:
            result += char
    return result

shift = int(input("Введите сдвиг шифрования: "))
text = input("Введите текст: ")

encrypted_text = caesar_cipher(shift, text)
print("Зашифрованный текст:", encrypted_text)

####

fruits = ('apple', 'banana', 'orange', 'banana', 'kiwi', 'banana')

fruit = input("Введите название фрукта: ")

count = fruits.count(fruit)

print("Количество раз, когда фрукт встречается:", count)


####

fruits = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')

fruit = input("Введите название фрукта: ")

count = 0
for item in fruits:
    if fruit in item:
        count += 1

print("Количество раз, когда название фрукта является частью элемента:", count)

####
cars = ('Ford', 'Toyota', 'Chevrolet', 'Toyota', 'Honda', 'Toyota')

production = input("Введите название производителя: ")
replacement = input("Введите слово для замены: ")

new_cars = tuple([replacement if x == production else x for x in production])

print("Измененный кортеж производителей автомобилей:", new_cars)


####


def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")


######


dictionary = {}

def add_word(dictionary, word, translation):
    dictionary[word] = translation
    print("Слово добавлено в словарь.")

def remove_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        print("Слово удалено из словаря.")
    else:
        print("Слово не найдено в словаре.")

def search_word(dictionary, word):
    if word in dictionary:
        print(f"Перевод слова '{word}': {dictionary[word]}")
    else:
        print("Слово не найдено в словаре.")

def replace_word(dictionary, word, new_translation):
    if word in dictionary:
        dictionary[word] = new_translation
        print("Перевод слова заменен.")
    else:
        print("Слово не найдено в словаре.")

add_word(dictionary, 'apple', 'pomme')
add_word(dictionary, 'banana', 'banane')
search_word(dictionary, 'apple')
replace_word(dictionary, 'apple', 'pomme')
search_word(dictionary, 'apple')
remove_word(dictionary, 'banana')
search_word(dictionary, 'banana')


####


def set_gen(numbers):
    result = set()
    count = {}
    for num in numbers:
        if num not in result:
            result.add(num)
        else:
            count[num] = count.get(num, 1) + 1
            result.add(str(num) * count[num])
    return result

numbers = [1, 2, 3, 4, 4, 4]

result_set = set_gen(numbers)
print(result_set)

####

import datetime
import json


current_date = datetime.datetime.now()


day1 = input("Введите первый день недели: ")
day2 = input("Введите второй день недели: ")


days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
try:
    day1_datetime = datetime.datetime.strptime(day1, '%A')
    day2_datetime = datetime.datetime.strptime(day2, '%A')
except ValueError:
    print("Некорректный ввод дня недели.")
    exit()


if day1_datetime == day2_datetime:
    print("Введены одинаковые дни недели.")
    exit()
elif day1_datetime > day2_datetime:
    greater_day = day1_datetime
    lesser_day = day2_datetime
else:
    greater_day = day2_datetime
    lesser_day = day1_datetime


hours_difference = (greater_day - lesser_day).total_seconds() / 3600


print("Осталось", hours_difference, "часов до наступления большей даты.")

# тут гпт чутка помог
data = {
    "day1": day1_datetime.strftime('%Y-%m-%d'),
    "day2": day2_datetime.strftime('%Y-%m-%d')
}

filename = "dates.json"
with open(filename, "w") as file:
    json.dump(data, file)

print("Даты записаны в файл", filename)



