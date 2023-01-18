import os
import MyModule

app_loop = True

# Чистим консоль, на 11 винде os.system('cls') не работает, увы.
def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")

# Главная входная функция, не обязательна, но задает тон хорошего программиста.
def main():
    # Нам нужно обзначить переменную глобальной, что бы далее получить к ней доступ
    global app_loop

    print("Здравствуйте, добро пожаловать на страницу авторизации уч. заведения TTHK.")
    act = input("Выберите ваше действие (1: Вход, 2: Регистрация, 3: Список пользователей, 4: Выход) => ")

    clear()

    if act == "1":
        MyModule.Login()
    elif act == "2":
        MyModule.Registration()
    elif act == "3":
        MyModule.ShowUsers()
    elif act == "4":
        app_loop = False
        return
    else:
        print("Действие не поддерживается.")

    print(f"\r")
    input("Press any key to continue..")

# Некое подобие Entry point, но на питоне, если пишем под компилятор то обязательно, в интерпритируемом же сегменте не важен, но задает хороший тон.
if __name__ == "__main__":
    # Ловим ошибки прямо на входе
    try:
        while app_loop:
            main()
            clear()
    # Выдаем исключение
    except:
        print("Что-то пошло не так.")

    print("Всего хорошего!")