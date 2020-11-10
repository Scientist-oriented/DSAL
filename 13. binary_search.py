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

# 이진 탐색을 검증하는 코드

total_count = 0
check_count = 0
function_count = 0

while total_count != 100:
    data_list = random.sample(range(10), 5)
    data_list.sort()


    if 3 in data_list:
        check_count += 1

    if binary_search(data_list, 3) == True:
        function_count += 1

    total_count += 1

print(total_count)
print(check_count)
print(function_count)

