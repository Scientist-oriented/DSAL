'''
# 문서검색

import sys
sys.stdin=open("input.txt", "rt")

document = input()
search_string = input()
result = 0

def count(docu, search):
    global result
    
    if len(docu) < len(search):
        return

    if docu[:len(search)] == search:
       result += 1
       return count(docu[len(search):], search)
    else:
        return count(docu[1:], search)

count(document, search_string)
print(result)
    # 재귀함수는 계산이 1000회 이하여야 함!
    # 이거는 재귀함수가 너무 많이 쌓여서 불가능 함!!!
    # 왠만하면 이런 한계를 생각하고 재귀함수가 아닌 것으로 코드 작성


# 문서검색
import sys
sys.stdin=open("input.txt", "rt")

document = input()
search = input()
result = 0

while len(document) >= len(search):
    if document[:len(search)] == search:
        result += 1
        document = document[len(search):]
    else:
        document = document[1:]

print(result)

# 새

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
k = 1
count = 0

while n > 0:
    n = n - k
    count += 1
    k += 1
    if n < k:
        k = 1

print(count)

'''
# 베스트셀러 문제

import sys
sys.stdin=open("input.txt", "rt")


N = int(input())
book_list = dict()

for _ in range(N):
    book = input()
    if book not in book_list:
        book_list[book] = 1
    else:
        book_list[book] += 1

sales_list = list()

for name, sales in book_list.items():
    sales_list.append((sales, name))

sales_list.sort()
sales_list = sorted(sales_list, key= lambda x : x[0], reverse=True)
print(sales_list[0][1])









