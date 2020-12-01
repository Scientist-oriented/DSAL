# 파이썬으로 해쉬함수를 갖춘 해쉬테이블 구현하기

hash_table = [0 for i in range(10)]
print(hash_table)

def hash_func(key):
    return key % 10

def hash_key(data):
    return hash(data)

def store_data(data, value):
    address = hash_func(hash_key(data))
    hash_table[address] = value

def get_data(data):
    address = hash_func(hash_key(data))
    print(hash_table[address])

store_data("Andy", "English")
store_data("Dave", "Math")
store_data("Cathy", "Korean")

print(hash_table)

get_data("Andy")
get_data("Dave")
get_data("Cathy")

# Chaining 기법 구현

def C_hash_func(key):
    return key % 3

def C_hash_key(data):
    return hash(data)

def C_store_data(data, value):
    C_address = C_hash_func(C_hash_key(data))

    if C_hash_table[C_address] != 0:
        for index in range(len(C_hash_table[C_address])):
            if C_hash_table[C_address][index][0] == C_hash_key(data):
                C_hash_table[C_address][index][1] = value
                return # 여기 리턴을 써야지 무의미한 for문 실행을 막을 수 있음.

        C_hash_table[C_address].append([C_hash_key(data), value]) # 이거를 for문 안에 넣어두면 돌 때마다 append해서 같은 요소가 여러 개 생김
    else:
        C_hash_table[C_address] = [[C_hash_key(data), value]]


def C_get_data(data):
    C_address = C_hash_func(C_hash_key(data))

    if C_hash_table[C_address] == 0:
        print("No value for the data")
        #return -> 반복문이 아니라 if문이라서 굳이 return을 쓸 필요가 없음

    elif len(C_hash_table[C_address]) == 1:
        print(C_hash_table[C_address][0][1])
        #return

    else:
        for index in range(len(C_hash_table[C_address])):
            if C_hash_table[C_address][index][0] == C_hash_key(data):
                print(C_hash_table[C_address][index][1])
                break

def C_delete_data(data):
    C_address = C_hash_func(C_hash_key(data))

    if C_hash_table[C_address] == 0:
        print("No data Can't delete")

    elif len(C_hash_table[C_address]) == 1:
        C_hash_table[C_address] = 0

    else:
        for index in range(len(C_hash_table[C_address])):
            if C_hash_table[C_address][index][0] == C_hash_key(data):
                del C_hash_table[C_address][index]
                break


print("--------------------Chaining Test------------------------")

C_hash_table = [0 for i in range(3)]
print(C_hash_table)

C_store_data("Andy", "English")
C_store_data("Dave", "Math")
C_store_data("Cathy", "Korean")

print(C_hash_table)

C_get_data("Andy")
C_get_data("Dave")
C_get_data("Cathy")

C_delete_data("Andy")

print(C_hash_table)

# Linear Probing 기법

LP_hash_table = [0 for i in range(4)]

def LP_hash_func(key):
    return key % 4

def LP_hash_key(data):
    return hash(data)

def LP_store_data(data, value):
    LP_key = hash(data)
    LP_address = LP_hash_func(LP_key)

    # 주피터 노트에 있는 if문이랑 아래 else문은 없어도 될 것 같음; 어차피 아래 반복문에서 LP_address부터 돌기 때문
    for index in range(LP_address, len(LP_hash_table)):
        if LP_hash_table[index] == 0:
            LP_hash_table[index] = [LP_key, value]
            return
        elif LP_hash_table[index][0] == data:
            LP_hash_table[index][1] = value
            return

def LP_get_data(data):
    LP_key = hash(data)
    LP_address = LP_hash_func(LP_key)

    for index in range(LP_address, len(LP_hash_table)):
        if LP_hash_table[index][0] == LP_key:
            print(LP_hash_table[index][1])
            return
        elif LP_hash_table[index] == 0:
            print("No value for the data")
            return

def LP_delete_data(data):
    LP_key = hash(data)
    LP_address = LP_hash_func(LP_key)

    for index in range(LP_address, len(LP_hash_table)):
        if LP_hash_table[index][0] == LP_key:
            LP_hash_table[index] = 0
            return
        elif LP_hash_table[index] == 0:
            print("No data Can't delete")
            return


print("--------------------LP Test----------------------")

print(LP_hash_table)

print(LP_hash_func(hash("Andy")))
print(LP_hash_func(hash("Dave")))
print(LP_hash_func(hash("Cathy")))

LP_store_data("Andy", "English")
LP_store_data("Dave", "Math")
LP_store_data("Cathy", "Korean")

print(LP_hash_table)

LP_get_data("Andy")
LP_get_data("Dave")
LP_get_data("Cathy")

LP_delete_data("Andy")

print(LP_hash_table)


# hashlib을 활용한 LP기법

import hashlib

HLP_hash_table = [0 for i in range(8)]

def HLP_hash_func(key):
    return key % 8

def HLP_hash_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def HLP_store_data(data, value):
    HLP_key = hash(data)
    HLP_address = HLP_hash_func(HLP_key)

    # 주피터 노트에 있는 if문이랑 아래 else문은 없어도 될 것 같음; 어차피 아래 반복문에서 HLP_address부터 돌기 때문
    for index in range(HLP_address, len(HLP_hash_table)):
        if HLP_hash_table[index] == 0:
            HLP_hash_table[index] = [HLP_key, value]
            return
        elif HLP_hash_table[index][0] == data:
            HLP_hash_table[index][1] = value
            return

def HLP_get_data(data):
    HLP_key = hash(data)
    HLP_address = HLP_hash_func(HLP_key)

    for index in range(HLP_address, len(HLP_hash_table)):
        if HLP_hash_table[index][0] == HLP_key:
            print(HLP_hash_table[index][1])
            return
        elif HLP_hash_table[index] == 0:
            print("No value for the data")
            return

def HLP_delete_data(data):
    HLP_key = hash(data)
    HLP_address = HLP_hash_func(HLP_key)

    for index in range(HLP_address, len(HLP_hash_table)):
        if HLP_hash_table[index][0] == HLP_key:
            HLP_hash_table[index] = 0
            return
        elif HLP_hash_table[index] == 0:
            print("No data Can't delete")
            return


print("--------------------Hashlib HLP Test----------------------")

print(HLP_hash_table)

print(HLP_hash_func(hash("Andy")))
print(HLP_hash_func(hash("Dave")))
print(HLP_hash_func(hash("Cathy")))

HLP_store_data("Andy", "English")
HLP_store_data("Dave", "Math")
HLP_store_data("Cathy", "Korean")

print(HLP_hash_table)

HLP_get_data("Andy")
HLP_get_data("Dave")
HLP_get_data("Cathy")

HLP_delete_data("Andy")

print(HLP_hash_table)

# 개선된 linear probing

hash_table = [0 for i in range(5)]
print(hash_table)

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 3

def show_address(data):
    print(hash(data) % 3)

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [key, value]

    else:
        if hash_table[address][0] == key:
            hash_table[address][1] = value
            return
            # 같은 data값에 다른 value를 덮어씌울 경우 이 코드가 없으면 안됨
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
        for index in range(0, address):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
        print("Full table")
def read(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        return "No data"
    elif hash_table[address][0] == key:
        return hash_table[address][1]
    else:
        for index in range(address+1, len(hash_table)):
            if hash_table[index] == 0:
                return "No data"
            elif hash_table[index][0] == key:
                return hash_table[index][1]
        for index in range(0, address):
            if hash_table[index] == 0:
                return "No data"
            elif hash_table[index][0] == key:
                return hash_table[index][1]
        return "No data"


save_data("Kim", "Korean")
save_data("Lee", "History")
save_data("Moon", "English")
save_data("Park", "Social Studies")
save_data("Kim", "Math")

print(hash_table)

show_address("Kim")
show_address("Lee")
show_address("Moon")

a = read("Kim")
b = read("Lee")
c = read("Moon")
d = read("Park")
e = read("Choi")

print(a, b, c, d, e)