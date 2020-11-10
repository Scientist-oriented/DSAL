# 순차탐색

def sequential_search(data, search):
    for index in range(len(data)):
        if data[index] == search:
            return index
    return -1

import random

data_list = random.sample(range(10), 5)
print(data_list)

a = sequential_search(data_list, 3)

print(a)

