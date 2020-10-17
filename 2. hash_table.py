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
                #return

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