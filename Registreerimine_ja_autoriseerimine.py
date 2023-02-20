import MyModule

# Kasutajate loendid
usernames = ['alice', 'bob', 'charlie']
passwords = ['password1', 'password2', 'password3']

# L�pmatu ts�kkel
while True:
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Nime v�i parooli muutmine")
    print("4. Unustasin parooli taastamine")
    print("5. L�petamine")
    valik = input("Vali tegevus: ")

    if valik == "1": # Registreerimine
        username = input("Sisesta kasutajanimi: ")
        if username in usernames:
            print("Kasutajanimi on juba kasutusel!")
        else:
            password_choice = input("Kas soovid ise parooli valida (V)�i lasta s�steemil genereerida parooli? ")
            if password_choice.lower() == "v":
                password = input("Sisesta parool: ")
                if not MyModule.validate_password(password):
                    print("Parool ei vasta n�uetele (peab sisaldama numbrit, v�ikest ja suurt t�hte, ning erim�rki)!")
                else:
                    usernames.append(username)
                    passwords.append(password)
                    print("Kasutaja registreeritud!")
            else:
                password = MyModule.generate_password()
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
            print("Autoriseerimine eba�nnestus!")

    elif valik == "3": # Nime v�i parooli muutmine
        username = input("Sisesta kasutajanimi: ")
        if username in usernames:
            password_choice = input("Kas soovid oma parooli muuta (V)�i kasutajanime muuta (K)? ")
            if password_choice.lower() == "v":
                new


