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