import os

def get_login_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password

def write_to_file(login, password):
    try:
        with open('credentials.txt', 'w') as file:
            file.write(f"Логин: {login}\nПароль: {password}\n")
        print("Логин и пароль успешно записаны в файл.")
    except IOError as e:
        print(f"Произошла ошибка при записи в файл: {e}")

if not os.path.exists('credentials_folder'):
    try:
        os.mkdir('credentials_folder')
        print("Папка 'credentials_folder' успешно создана.")
    except OSError as e:
        print(f"Произошла ошибка при создании папки: {e}")

os.chdir('credentials_folder')

login, password = get_login_password()

write_to_file(login, password)
