print("Программа выводит какой год висакаосный или обычный")

year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} - Високосный год")
else:
    print(f"{year} - обычный год")