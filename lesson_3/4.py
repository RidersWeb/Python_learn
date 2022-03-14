print('Программа считает произведение всех введенных чисел')
print('============================================')
print('Что бы остановить программу введите команду exit')

while True:
    numbers = input('Введите числа через запятую которые хотите посчитать: ')
    arr_num = numbers.split(',')
    if len(arr_num) == 1:
        if arr_num[0] == 'exit':
            print("Завершение программы")
            break
        else:
            print(f"Вы ввели одно число {numbers[0]}")
    else:
        result = 1
        for num in arr_num:
            num = int(num)
            result *= num
        print(f'Сумма Ваших чисел равна  = {result}')