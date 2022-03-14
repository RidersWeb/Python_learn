print("- Программа определяет делится число на 6")
print("Для завершение программы в консоль напишите команду exit")
print('========================================================')

num = 6

while True:
    number = input(f"В ведите число я проверю делится число на {num} или нет: ")
    if number == "exit":
        print("Вы Завершили программу")
        break
    else:
        try:
            number = int(number)
            if type(number) == int:
                if (number % num) == 0:
                    print(f"Число делится на {num}")
                else:
                    print(f"Число НЕ делится на {num}")
        except:
            print("Вы ввели не число, перезапустите программу")
            break  