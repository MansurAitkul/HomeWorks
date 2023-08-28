def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Ввод пользователей
phrase1 = input("Введите первую фразу: ")
phrase2 = input("Введите вторую фразу: ")

if is_anagram(phrase1, phrase2):
    print("Это анаграммы!")
else:
    print("Это не анаграммы.")
