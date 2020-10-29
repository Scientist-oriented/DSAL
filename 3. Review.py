# 해쉬테이블

hash_table = [0 for i in range(10)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 10

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [[key, value]]

    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                hash_table[address][index][1] = value
                return
        
        hash_table[address].append([key, value])
            


def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    return hash_table[address]

save_data("KIm", "Korea")
save_data("Johnson", "USA")
save_data("Yamamoto", "Japan")

print(hash_table)

print(read_data("KIm"))
print(read_data("Johnson"))
print(read_data("Yamamoto"))

