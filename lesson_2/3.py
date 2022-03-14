import re

print("Программа пересчитывает граммы, килограммы и тонны")
print("---------------------------------------")

text = input('Введите число и без пробела единицу измерения 12kg: ' )

num = "".join(re.findall(r'[0-9][\.]?\d+', text))
ves = re.sub(r'[^\w\s]+|[\d]+', r'', text).strip()

if ves == 'kg':
    num = int(num)
    print(f'{round(num * 1000)}g')
    print(f'{round(num / 1000)}t')
elif ves == 'g':
    num = int(num)
    print(f'{num / 1000}kg')
    print(f'{num / 1000000}t')
elif ves == 't':
    num = float(num)
    print(f'{round(num * 1000)}kg')
    print(f'{round(num * 1000000)}g')
else:
    print("В меня не заложили такие данные, обратитесь к моему разработчику")