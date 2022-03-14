str_1 = input('Введите строку или нажмите Enter будет строка по дефолту I loovee Pyythhonn!!!!! \n') or 'I loovee Pyythhonn!!!!!'

str_2 = ''

for i, char in enumerate(str_1):
    count = str_1[i-1]
    if count != char:
        str_2 += char

print("Убрали все дубли: ", str_2)