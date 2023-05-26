a = int(input("Введите стоимость подписки: "))
b = int(input("Введите чстоимость пиццы: "))
c = int(input("Введите запрплату Васи: "))


if a + b > c:
    print("Нет")
else:
    print("Да")

##############################################################
def checking(a, b, c):

    if a + b <= c:
        return True
    else:
        return False

a = int(input("Введите стоимость подписки: "))
b = int(input("Введите стоимость пиццы: "))
c = int(input("Введите зарплату: "))

if checking(a, b, c):
    print("Да")
else:
    print("Нет")