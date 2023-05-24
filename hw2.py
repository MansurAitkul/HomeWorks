login = input("Введите логин: ")
password = input("Введите пароль: ")


correct_login = "ilyas"
correct_password = "qwerty"

if login == correct_login and password == correct_password:
    print("Authentication completed")
else:
    print("Invalid login or password")

#################################################

a = {
    'USD': 420,
    'EUR': 510,
    'RUB': 5.8
}

tenge = float(input("Введите сумму в тенге: "))
current = input("Выберите валюту (USD, EUR, RUB): ")

if current in a:
    b = a[current]
    convert = tenge / b
    print("Полученная сумма: {:.2f} {}".format(convert, current))
else:
    print("Выбрана недопустимая валюта.")


###########################################################

numbers = []
qvadrat = []

for a in range(1000+1):
    numbers.append(a)
    qavdrat.append(a ** 2)


print("Массив чисел:", numbers)
print("Массив квадратов чисел:", squares)