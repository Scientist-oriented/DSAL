# 이진 탐색

def binary_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    
    if len(data) == 1 and data[0] != search:
        return False

    if len(data) == 0:
        return False

    medium = len(data) // 2
    if data[medium] == search:
        return True
    else:
        if data[medium] < search:
            return binary_search(data[medium+1:], search)
        else:
            return binary_search(data[:medium], search)

# 테스트

import random
data_list = random.sample(range(10), 5)
data_list.sort()
print(data_list)

a = binary_search(data_list, 3)
print(a)

