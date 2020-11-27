'''
# SHA-256

import hashlib
string = str(input())
data = string.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# 수찾기 문제



num_n = int(input())
n_set = set(map(int, input().split()))
num_m = int(input())
m_list = list(map(int, input().split()))

for data in m_list:
    if data in n_set:
        print(1)
    else:
        print(0)


# 친구네트워크 문제

import sys
sys.stdin=open("input.txt", "rt")

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if root1 != root2:
        parent[root2]  = root1
        number[root1] += number[root2]

def make_set(node):
    parent[node] = node
    number[node] = 1

test_case = int(input())

for _ in range(test_case):
    f = int(input())
    parent = dict()
    number = dict()
    for _ in range(f):
        node_u, node_v = input().split(' ')

        if node_u not in parent:
            make_set(node_u)

        if node_v not in parent:
            make_set(node_v)

        union(node_u, node_v)

        print(number[find(node_u)])
        # 어차피 node_u와 node_v는 연결된 상태이기 때문에 둘 중에 아무거나 number 출력하면 됨

'''