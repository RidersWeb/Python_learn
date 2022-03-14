stroka = '2122234555768290909389'
list_ = []

def count_it(stroka):
    for key in range(0, 10):
        list_.append(int(stroka.count(str(key))))
        
    print(list_)



count_it(stroka)