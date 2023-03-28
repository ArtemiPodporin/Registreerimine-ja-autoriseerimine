import module1

# Kasutajate loendid
usernames = ['alice', 'bob', 'charlie']
passwords = ['password1', 'password2', 'password3']

# Lõpmatu tsükkel
while True:
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Nime või parooli muutmine")
    print("4. Unustasin parooli taastamine")
    print("5. Lõpetamine")
    valik = input("Vali tegevus: ")

    if valik == "1": # Registreerimine
        username = input("Sisesta kasutajanimi: ")
        if username in usernames:
            print("Kasutajanimi on juba kasutusel!")
        else:
            password_choice = input("Kas soovid ise parooli valida (V)õi lasta süsteemil genereerida parooli? ")
            if password_choice.lower() == "v":
                password = input("Sisesta parool: ")
                if not module1.validate_password(password):
                    print("Parool ei vasta nõuetele (peab sisaldama numbrit, väikest ja suurt tähte, ning erimärki)!")
                else:
                    usernames.append(username)
                    passwords.append(password)
                    print("Kasutaja registreeritud!")
            else:
                password = module1.generate_password()
                print("Genereeritud parool: ", password)
                usernames.append(username)
                passwords.append(password)
                print("Kasutaja registreeritud!")

    elif valik == "2": # Autoriseerimine
        username = input("Sisesta kasutajanimi: ")
        password = input("Sisesta parool: ")
        if username in usernames and password == passwords[usernames.index(username)]:
            print("Autoriseeritud kasutaja:", username)
        else:
            print("Autoriseerimine ebaõnnestus!")

    elif valik == "3": # Nime või parooli muutmine
        username = input("Sisesta kasutajanimi: ")
        if username in usernames:
            password_choice = input("Kas soovid oma parooli muuta (V)õi kasutajanime muuta (K)? ")
            if password_choice.lower() == "v":
                new_password = input("Введите новый пароль: ")
                if not module1.validate_password(new_password):
                    print("Пароль не соответствует требованиям (должен содержать цифры, заглавные и строчные буквы, а также специальный символ)!")
                else:
                    passwords[usernames.index(username)] = new_password
                    print("Пароль изменен!")
            elif password_choice.lower() == "и":
                new_username = input("Введите новое имя пользователя: ")
                if new_username in usernames:
                    print("Это имя пользователя уже занято!")
                else:
                    usernames[usernames.index(username)] = new_username
                    print("Имя пользователя изменено!")
            else:
                print("Некорректный ввод!")
        else:
            print("Такое имя пользователя не существует!")
    elif valik == "4": # Восстановление пароля
        username = input("Введите имя пользователя: ")
        if username in usernames:
            new_password = module1.generate_password()
            passwords[usernames.index(username)] = new_password
            print("Ваш новый пароль: ", new_password)
        else:
            print("Такое имя пользователя не существует!")
    elif valik == "5": # Выход из программы
        print("До свидания!")
        break



