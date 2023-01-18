import random

user_arr = dict()

def gen_passwd(plen: int):
    str0 = ".,:;!_*-+()/#§%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3

    ls = list(str4)
    random.shuffle(ls)

    # Извлекаем из списка plen произвольных значений, и возвращаем готовый пароль
    return ''.join([random.choice(ls) for x in range(plen)])

def chk_passwd(passwd: str):
    if (passwd == "" or len(passwd) < 8):
        print("Password is empty too short.")
        return False # empty password

    if not any(char.isdigit() for char in passwd):
        print("No digit.")
        return False # low quality

    if not any(char.isupper() for char in passwd):
        print("No upper character.")
        return False # low quality

    if not any(char.islower() for char in passwd):
        print("No lower character.")
        return False # low quality

    if not any(char in ".,:;!_*-+()/#§%&" for char in passwd):
        print("No special character.")
        return False # low quality

    return True # OK

def ShowUsers():
    if len(user_arr) == 0:
        print("Пользователей нет.")
        return

    print("Пользователи системы:")
    for u, passwd in user_arr.items():
        print(f"User \"{u}\": {passwd}")

    return

def Login():
    print("Здравствуйте, добро пожаловать в форму входа уч. заведения TTHK.")

    tmp_login = input("Введите логин => ")
    tmp_passwd = input("Введите пароль => ")

    if not tmp_login in user_arr:
        print(f"Пользователь не найден.")
        return
    elif user_arr.get(tmp_login) != tmp_passwd:
        print(f"Не верный пароль.")
        return
    
    print("Вход успешен.")
    return

def Registration():
    print("Здравствуйте, добро пожаловать в рег. форму уч. заведения TTHK.")

    try_ = 0
    while try_ < 3:
        tmp_login = input("Введите логин для регистрации => ")
        if tmp_login in user_arr:
            print(f"Данный пользователь уже существует, попробуйте заного (осталось попыток {3 - try_ - 1})")
            try_ += 1
            continue
        elif len(tmp_login) > 1:
            break

    if try_ == 3:
        print("Попробуйте еще раз.")
        return

    try_ = 0
    while try_ < 3:
        tmp_passwd = input("Введите пароль (оставьте пустым для автогенерации) => ")
        if tmp_passwd == "":
            tmp_passwd = gen_passwd(12)
        elif chk_passwd(tmp_passwd) != True:
            print(f"Слабый пароль, пароль должен содержать одну строчную букву, одну цифру и один символ, и быть не менее 8 символов. (Осталось попыток: {3 - try_ - 1})")
            try_ += 1
            continue

        break

    if try_ == 3:
        print("Попробуйте еще раз.")
        return

    user_arr.update({ tmp_login: tmp_passwd })
    print(f"Пользователь {tmp_login} успешно зарегистрирован, ваш пароль : {tmp_passwd}")
    print(f"\r")

    print("Пользователи системы:")
    for u, passwd in user_arr.items():
        print(f"User \"{u}\": {passwd}")

    return