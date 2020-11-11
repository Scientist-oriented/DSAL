# 탐욕알고리즘 구현

# 동전문제

coin_list = [1, 100, 50, 500]
coin_list.sort(reverse=True)
print(coin_list)

def min_coin_count(value, coin_list):
    coin_count = 0
    details = list()

    for coin in coin_list:
        coin_num = value // coin
        coin_count += coin_num

        details.append([coin, coin_num])
        value -= coin * coin_num

    return coin_count, details

a = min_coin_count(4720, coin_list)
print(a)

# 탐욕알고리즘: 부분배낭문제

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            total_value += data[1]
            capacity -= data[0]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details

a = get_max_value(data_list, 30)
print(a)