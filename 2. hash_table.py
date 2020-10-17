# 파이썬으로 해쉬함수를 갖춘 해쉬테이블 구현하기

hash_table = [0 for i in range(10)]
print(hash_table)

def hash_func(key):
    return key % 10

def hash_key(data):
    return hash(data)

def store_data(data, value):
    key = hash_func(hash_key(data))
    hash_table[key] = value

def get_data(data):
    key = hash_func(hash_key(data))
    print(hash_table[key])

store_data("Andy", "English")
store_data("Dave", "Math")
store_data("Cathy", "Korean")

print(hash_table)

get_data("Andy")
get_data("Dave")
get_data("Cathy")