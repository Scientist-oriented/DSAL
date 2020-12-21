# 삽입 정렬

def insertsort(data):
    for index in range(len(data)-1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

insertsort(Testlist)
print(Testlist)

