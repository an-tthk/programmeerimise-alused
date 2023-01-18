# Импортируем библиотеки
import random

# Делаем словарь глобальным
user_arr = dict()

# Генерация случайного пароля
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

# Проверка пароля на прочность по критериям
def chk_passwd(passwd: str):
    # Если пароль отсутствует или менее 8 символов
    if (passwd == "" or len(passwd) < 8):
        print("Password is empty too short.")
        return False
    # Если нет цифр в пароле
    if not any(char.isdigit() for char in passwd):
        print("No digit.")
        return False
    # Если нет uppercase буквы
    if not any(char.isupper() for char in passwd):
        print("No upper character.")
        return False
    # Если нет lowercase буквы
    if not any(char.islower() for char in passwd):
        print("No lower character.")
        return False
    # Если нет спецсимволов
    if not any(char in ".,:;!_*-+()/#§%&" for char in passwd):
        print("No special character.")
        return False
    # Иначе возвращаем что всё хорошо
    return True

# Вывод списка пользователей в консоль
def ShowUsers():
    # Если словарь пустой, то пользователей еще нет
    if len(user_arr) == 0:
        print("Пользователей нет.")
        return
    # Возвращаем список пользователей системы и их пароль
    print("Пользователи системы:")
    for u, passwd in user_arr.items():
        print(f"User \"{u}\": {passwd}")

    return

# Вход в систему (эмуляция)
def Login():
    print("Здравствуйте, добро пожаловать в форму входа уч. заведения TTHK.")

    tmp_login = input("Введите логин => ")
    tmp_passwd = input("Введите пароль => ")

    # Проверяем есть ли у нас такой пользователь
    if not tmp_login in user_arr:
        print(f"Пользователь не найден.")
        return
    # Если пользователь присутствует, проверяем верный ли пароль
    elif user_arr.get(tmp_login) != tmp_passwd:
        print(f"Не верный пароль.")
        return
    
    # Если всё верно, то мы успешно вошли
    print("Вход успешен.")
    return

# Регистрация в системе (эмуляция)
def Registration():
    print("Здравствуйте, добро пожаловать в рег. форму уч. заведения TTHK.")

    # Три попытки на регистрацию, проверка уже существующего пользователя в системе и кол-во символов хотя бы > 1
    try_ = 0
    while try_ < 3:
        tmp_login = input("Введите логин для регистрации => ")
        if tmp_login in user_arr:
            print(f"Данный пользователь уже существует, попробуйте заного (осталось попыток {3 - try_ - 1})")
            try_ += 1
            continue
        elif len(tmp_login) > 1:
            break

    # Если 3 попытки использовали, выходим (тут нужно вешать бан по ip, чтоб не брутфорсили :))
    if try_ == 3:
        print("Попробуйте еще раз.")
        return

    # Три попытки на регистрацию, проверка уже пароля на прочность, либо автогенерация
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

    # Если 3 попытки использовали, выходим (так же баним по ip как и выше при не верном логине)
    if try_ == 3:
        print("Попробуйте еще раз.")
        return

    user_arr.update({ tmp_login: tmp_passwd })
    print(f"Пользователь {tmp_login} успешно зарегистрирован, ваш пароль : {tmp_passwd}")
    print(f"\r")

    return