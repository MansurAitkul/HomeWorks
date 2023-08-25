def plus_two(number):
    try:
        result = 2 + number
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")

plus_two(3)  
plus_two("4")  

