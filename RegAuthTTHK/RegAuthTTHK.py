import os
import MyModule

def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")

def main():

    print("Здравствуйте, добро пожаловать на страницу авторизации уч. заведения TTHK.")
    act = input("Выберите ваше действие (1: Вход, 2: Регистрация, 3: Список пользователей) => ")

    clear()

    if act == "1":
        MyModule.Login()
    elif act == "2":
        MyModule.Registration()
    elif act == "3":
        MyModule.ShowUsers()
    else:
        print("Действие не поддерживается.")

    print(f"\r")
    input("Press any key to continue..")

if __name__ == "__main__":
    try:
        while(True):
            main()
            clear()
    except:
        print("Что-то пошло не так.")