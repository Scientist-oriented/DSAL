# 거스름돈 문제

changes = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10, 5, 1]:
    count += changes // i
    changes %= i

print(count)

# 뒤집기

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
    # 맨 처음이 1이면 0으로 만들기 위해서 1번은 뒤집어야
if data[0] == '0':
    count1 += 1
    # 마친가지로 0일 때도

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 연속된 것은 한꺼번에 뒤집을 수 있으므로
        # 연속되지 않은 경우만 count해주면 된다!
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

# 등수 매기기
    # 아이디어만 떠올릴 수 있다면 구현은 아주 쉬운 문제

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()
    # 그리디 알고리즘은 정렬과 많이 쓰임

result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])

print(result)

# 배 문제

import sys

n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    sys.exit()
    # 크레인이 옮길 수 없는 박스가 있는지 확인

position = [0] * n
checked = [False] * m

cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(boxes):
        break
        # 박스를 다 옮겼다면 반복문 종료
    for i in range(n):
        while position[i] < len(boxes):
            if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    result += 1

print(result)