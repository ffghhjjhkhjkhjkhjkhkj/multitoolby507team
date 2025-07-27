import os

print("Привет! спасибо за установку мультитула от 507-team")
print("Что вы хотите сделать?")
print("")
print("1: Обновить систему")
print("2: Установка ПО")
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