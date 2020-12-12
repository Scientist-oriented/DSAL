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
# 각각의 크레인이 지금 옮겨야 하는 박스의 번호
checked = [False] * m
# 각 박스를 옮겼는지 여부를 저장

cranes.sort(reverse=True)
# 힘 좋은 크레인부터 쓰기 위해 역순 정렬
boxes.sort(reverse=True)
# 무거운 박스부터 옮기기 위해 역순 정렬

result = 0
count = 0

while True:
    # 반복문이 한번 돌 때마다 1분
    if count == len(boxes):
        break
        # 박스를 다 옮겼다면 반복문 종료
    for i in range(n):
        # 매분마다 모든 크레인을 확인
        while position[i] < len(boxes):
            # 박스 번호가 전체 박스 개수와 같아지면 더 이상 나를 수 있는 가벼운 박스가 없는 것
            if not checked[position[i]] and cranes[i] >= boxes[position[i]]:
                # 현재 박스가 아직 안 옮겨졌고, 크레인이 그 박스를 옮길 수 있으면
                checked[position[i]] = True
                # 그 박스를 옮겼다고 체크하고
                position[i] += 1
                # 다음 박스를 옮길 차례라고 체크하고
                count += 1
                # 총 옮긴 박스의 갯수도 추가
                break
            position[i] += 1
            # 박스번호를 늘려가면서 (= 점점 가벼운 박스로 가면서) 탐색
    result += 1
    # 매분 지날 때마다 체크

print(result)