import os

print("Привет! спасибо за установку мультитула от 507-team")
print("Что вы хотите сделать?")
print("")
print("1: Обновить систему")
print("2: Установка ПО")
print("3: Инфо о системе")
print("")
print("Напишите цифру: ")
choice = input()

if choice == "1":
    print("Идет обновление... Выполняеться sudo apt upgrade")
    os.system("sudo apt upgrade")
    print("Выполняеться sudo apt update...")
    os.system("sudo apt update")
    print("Обнова завершена!!")

if choice == "2":
    print("Выберите ПО для установки")
    print("")
    print("1: Chrome (им кто то на линуксе пользуется?)) ")
    print("2: Firefox (А нафига если вроде в системе он и так устанавливаеться стандартно?)")
    print("3: Steam (для геймеров)")
    print("4: docker (для... незнаю кого)")
    print("5: hollywood (не ну а че?)")
    print("0: Категории (BETA)")
    print("")
    print("Введите цифру:")
    install = input()
    if install == "1":
        print("Установка chrome...")
        os.system("sudo apt install google-chrome-stable")
        print("Все хром готов")
    if install == "2":
        print("Ну ладно установлю я твою огненую лису..")
        os.system("sudo apt install firefox")
        print("Все огненая лиса установлена")

    if install == "3":
        print("Устанавливаю стим...")
        os.system("sudo apt-get install steam")
        print("Стим установлен!")

    if install == "4":
        print("Устанавливаю докер...")
        os.system("sudo apt install docker")
        print("Докер готов.")

    if install == "5":
        print("Устанавливаю hollywood...")
        os.system("sudo apt install hollywood") 
        print("Готово")
    if install == "0":
        print("Категории:")
        print("")
        print("[1]: Браузеры")
        print("[2]: Гейминг")
        print("[3]: Для сис админов")
        print("")
        print("Выберите категорию:")
        kategorii = input()

        if kategorii == "1":
            print("Вот список программ в категории [Браузеры]:")
            print("")
            print("1: Chrome")
            print("2: firefox")
            print("")
            print("Выберите программу:")
            brow = input()
            if brow == "1":      
                print("Установка chrome...")
                os.system("sudo apt install google-chrome-stable")
                print("Все хром готов")

        if kategorii == "2":
            print("Вот список программ в категории [Гейминг]:")
            print("")
            print("1: Steam")
            print("")
            print("Выберите программу:")
            geiming = input()
            if geiming == "1":      
                print("Устанавливаю стим...")
                os.system("sudo apt-get install steam")
                print("Стим установлен!")

        if kategorii == "3":
            print("Вот список программ в категории [Для сис админов]:")
            print("")
            print("1: docker")
            print("")
            print("Выберите программу:")
            sis = input()
            if sis == "1":      
                print("Устанавливаю докер...")
                os.system("sudo apt install docker")
                print("Докер готов.")
                
if choice == "3":
    os.system("neofetch")
