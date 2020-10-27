# 선택정렬

def selectionsort(data):
    for stand in range(len(data)-1):
        lowest = stand 
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]


import random

Testlist = random.sample(range(100), 50)
print(Testlist)

selectionsort(Testlist)
print(Testlist)