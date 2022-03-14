number = int(input('Input number: '))

i = 1
factorial = 1

# Факториал с помощью while

# while i <= number:
#     factorial *= i
#     i += 1
# print(factorial)


# Факториал с помощью for
for i in range(1, number + 1):
    factorial *= i
print(factorial)