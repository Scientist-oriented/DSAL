'''
# 수 정렬하기
import sys
sys.stdin=open("input.txt", "rt")

number = int(input())
data_list = []
for _ in range(number):
    data_list.append(int(input()))

data_list.sort() 

# 파이썬 기본 정렬 알고리즘의 시간복잡도
 = O(nlogn)

for data in data_list:
    print(data)

# 소트인사이드
import sys
sys.stdin=open("input.txt", "rt")

string = str(input())
data_list = list()

# 자릿수 이니까 0 ~9까지 counting하는 방법이 더 나음

for data in string:
    data_list.append(int(data))

data_list.sort(reverse=True)

for data in data_list:
    print(data, end='')



# 나이순 정렬

import sys
sys.stdin=open("input.txt", "rt")

member_number = int(input())
member_list = list()

for _ in range(member_number):
    age, name = map(str, input().split(' '))
    member_list.append((int(age), name))

for age in range(1, 201):
    for member in member_list:
        if age == member[0]:
            print(member[0], member[1])

# 중요필기: sorted의 속성
array = {(3, "b"), (3, "a"), (2, "d"), (2, "c")}

array = sorted(array, key=lambda x: x[0]) 
    # 여기서는 x[0]만 가지고 정렬 나머지는 원래 순서대로 (stable 속성)
array = sorted(array)
    # 이 경우에는 x[0]을 가지고 정렬하고 더 나아가서 x[1]도 알파벳 순으로 정렬


# 좌표 정렬하기

import sys
sys.stdin=open("input.txt", "rt")

number = int(input())
data_list = list()

for _ in range(number):
    x, y = map(int, input().split(' '))
    data_list.append((x, y))

def qsort(data_list):
    if len(data_list) <= 1:
        return data_list

    pivot = data_list[0]
    left = []
    right = []

    for index in range(1, len(data_list)):
        if data_list[index][0] < pivot[0]:
            left.append(data_list[index])
        elif data_list[index][0] > pivot[0]:
            right.append(data_list[index])
        else:
            if data_list[index][1] < pivot[1]:
                left.append(data_list[index])
            else:
                right.append(data_list[index])

    return qsort(left) + [pivot] + qsort(right)

data_list = qsort(data_list)        

for data in data_list:
    print(data[0], data[1])

'''
# 수 정렬하기 3
    # 파이썬의 1초에 2000만회의 연산
    # 기본정렬 알고리즘 nlogn
    # counting sort : 계수 정렬 알고리즘을 사용해야 함.
    # 데이터의 갯수가 많으면 sys.stdin.readline() 사용

import sys
sys.stdin=open("input.txt", "rt")

number = int(sys.stdin.readline())
counting_list = [0] * 10001

for _ in range(number):
    data = int(sys.stdin.readline())
    counting_list[data] += 1

for index in range(len(counting_list)):
    if counting_list[index] != 0:
        for _ in range(counting_list[index]):
            print(index)









