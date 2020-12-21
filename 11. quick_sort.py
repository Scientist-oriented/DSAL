# 퀵정렬 구현

def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = list()
    right = list()

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)

import random

data_list = random.sample(range(100), 10)

print(data_list)
a = qsort(data_list)
print(a)
    # return이 포함된 함수를 print할 때는 이런 절차를 거쳐야 한다.

# list comprehension을 사용한 방법

def q_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return q_sort(left) + [pivot] + q_sort(right)

data_list = random.sample(range(100), 10)

print(data_list)
b = q_sort(data_list)
print(b)