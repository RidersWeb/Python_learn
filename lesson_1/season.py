print("Для завершения программы введите exit")
print("=====================================")


month = input('Введите номер месяца: ')
season = ["Зима", "Весна", "Лето", "Осень"]

while True:
    if not month:
        month = input('Хотите продолжить? Введите номер или Нет: ')

    if month == 'exit' or month == 'Нет' or month == 'Ytn':
        print("Завершение программы")
        break

    else:
        try:
            month = int(month)
            if(month == 12 or month == 1 or month == 2):
                print(season[0])
                month = ''
            elif(month == 3 or month == 4 or month == 5):
                print(season[1])
                month = ''
            elif(month == 6 or month == 7 or month == 8):
                print(season[2])
                month = ''
            elif(month == 9 or month == 10 or month == 11):
                print(season[3])
                month = ''
            else:
                print("Такого месяца нет!")
                month = ''
        except:
            print("Вы ввели не допустимое значение, перезапустите программу и попробуйте ещё раз :)")
            break