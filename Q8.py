'''
# 공유기 문제

import sys
sys.stdin=open("input.txt", "rt")

n, c = list(map(int, input().split(' ')))

array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

max_gap = array[-1] - array[0]
min_gap = array[1] - array[0]
result = 0
    # 좌표는 중요하지 않고 해당되는 gap이 공유기를 설치할 수 있는지 없는지가 중요함.
    # gap을 중심으로 생각하자!

    # 반복문을 통한 이진탐색구현 
        # 최소/최대를 계속 좁혀가면서 반복
        # 끝나는 조건은 최소/최대가 붙었을 때
while(max_gap >= min_gap):
    current_gap = (max_gap + min_gap) // 2
    start_point = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= start_point + current_gap:
            start_point = array[i]
            count += 1
    if count >= c:
        min_gap = current_gap + 1
        # 공유기를 설치할 수 있으므로 이 gap 이상으로 설치할 수 있는지 확인
        result = current_gap
    else:
        max_gap = current_gap - 1
        # 공유기를 설치할 수 없으므로 이 gap보다 낮은 단계에서 다시 이진탐색

print(result)
'''
# 중량제한 문제

import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def dfs(c):
    # 중량을 입력하면 그 중량으로 end_node에 갈 수 있는지 확인해주는 함수
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True
    
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            # 인접node와 weight를 튜플에서 받아와서
            if not visited[y] and weight >= c:
                # 안갔는지, 그리고 갈 수 있는 곳인지 체크
                # 여기서 최소값을 구하는게 아니므로 되는지 안되는지만 체크하면 됨
                    # 일종의 분할정복
                visited[y] = True
                queue.append(y)
    
    return visited[end_node]

start = 1000000000
end = 1
    # start가 가장 작은 weight로 구할 수 있도록 설정
    # end가 가장 큰 weight를 구할 수 있도록 설정

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
        # adj에 데이터를 저장하고
    start = min(start, weight)
    end = max(end, weight)
        # 탐색해야하는 범위를 좁힌다.
        # 이진탐색의 시작점: weight 중에 가장 작은 것
        # 이진탐색의 끝점: weight 중에 가장 큰 것

start_node, end_node = map(int, input().split(' '))

result = start

while start <= end:
    current_weight = (start + end) // 2
    if dfs(current_weight):
        result = current_weight
        start = current_weight + 1
    else:
        end = current_weight - 1

print(result)


