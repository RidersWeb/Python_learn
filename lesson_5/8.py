nums = [2, 4, 6, 8, 10]
multi = 2

def multi_num(nums, multi):
    l_num = []
    i = 0
    for num in nums:
        if num%4 == 0:
            l_num.append(num * multi)
            i += 1
    return i, l_num 
i , l_num = multi_num(nums, multi)
print(f'Программа нашла - {i} числа и умножила их на {multi}')
print(f'Ответ: {l_num}')
