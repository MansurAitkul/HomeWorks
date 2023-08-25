import hashlib

def save_password(login, password):

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('passwords.txt', 'a') as file:
        file.write(f"Login: {login}, Hashed Password: {hashed_password}\n")


login = input("Введите логин: ")
password = input("Введите пароль: ")


save_password(login, password)

print("Пароль успешно сохранен.")
