text =  input("Введите строкну: \n")
result = 0
for str in text:
    if str.isupper():
        result += 1
print(f'В этом тексте заглавных букв - {result}')