import re
print("Введите текст заменив букву ее цифровым значением, программ переведет в текст")
stroka = input('Или нажмите Enter деффолтовое значение "H4l12o 16e15ple" ') or 'H4l12o 16e15ple'
res_num = ''
result = ''
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i, num in enumerate(stroka):
    if re.findall(r'\d', num):
        i += 1
        if re.findall(r'\d', stroka[i]):
            a = int(num + stroka[i])
            result += char_list[a-1]
            i += 1
        elif not(re.findall(r'\d', stroka[i-2])):
            a = int(num)
            result += char_list[a]
        
    else:
        result += num
        i += 1

print(result)