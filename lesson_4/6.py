# # Задание 1
print('Программа 1')
number = list(range(10, 46, 5))
print(number)

# Задание 2
print('Программа 2')
i = 1
while i <= 5:
    print(i)
    i += 1

# # Задание 3 - вариант 1
print('Программа 3/1')
stroka = '123467'
count = 0
l_num = list(range(int(stroka[0]), int(stroka[-1]) + 1))
num = ''
while count < len(l_num):
    num += str(l_num[count])
    count = count + 1
print(num)
    
# # Задание 3 Вариант 2
print('Программа 3/2')
stroka1 = '123467'
count = 0
l_num = list(range(int(stroka[0]), int(stroka[-1]) + 1))
print("".join(map(str, l_num)))

# Задание 4
print('Программа 4')
stroka_4 = 'Если долго будешь писать на питоне - начнёшь говорить со змеями'
str_char = 'о'
i = 0
for char in stroka_4:
    if char == str_char or char == str_char.upper():
        i += 1
print(f'В строке букв {str_char} - {i} штук')