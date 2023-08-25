def check_name(names, target):
    i = 0
    while i < len(names):
        if names[i] == target:
            return True
        i += 1
    return False



names = ['Aruzhan', 'Egor', 'Mansur', 'Genadiy']
target = 'Mansur'

result = check_name(names, target)
print(result)