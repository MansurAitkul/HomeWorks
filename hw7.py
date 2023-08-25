#2 zadanie

numbers = []
while True:
    num = int(input("Введите число: "))
    numbers.append(num)
    if sum(numbers) == 0:
        break

sum_of_squares = sum([x ** 2 for x in numbers])
print("Сумма квадратов введенных чисел:", sum_of_squares)


#####


# 1 zadanie
grades = input("Введите список оценок через пробел: ").split()


fives = grades.count("5")
fours = grades.count("4")
threes = grades.count("3")
twos = grades.count("2")


print(f"{fives} {fours} {threes} {twos}")


total_sum = sum(int(grade) for grade in grades)
average = total_sum / len(grades)


print(average)


######
#pdf

import re

def register_user():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    email = input("Введите адрес электронной почты: ")

    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
        print("Ошибка: Пароль должен содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Ошибка: Некорректный адрес электронной почты.")
        return

    print("Пользователь успешно зарегистрирован.")
    
register_user()


####

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

even_posts = [post for post in posts if post['id'] % 2 == 0]
print(even_posts)
