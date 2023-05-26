
a = int(input("Введите сторону 1: "))
b = int(input("Введите сторону 2: "))
c = int(input("Введите сторону 3: "))


if a + b > c and a + c > b and b + c > a:
    result = True
else:
    result = False


print(result)


##########################################

a = int(input("Введите число a: "))


if a % 2 == 0:
    b = True
else:
    b = False

print(b)

##########################################

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))


if a + b > c:
    konec = True
else:
    konec = False

print(konec)

###########################################


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    c = True
else:
    c = False

print(c)