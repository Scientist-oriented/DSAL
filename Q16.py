'''
# 해킹 문제

import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    # 우선순위큐에는 간선의 cost가 앞으로 가도록 저장
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    # 컴퓨터 개수에 만큼 adj 만든다
    distance = [1e9] * (n + 1)
    for _ in range(m):
        # 간선을 adj에 저장
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distance:
        if i !=1e9:
            count += 1
            # distance가 inf가 아니면 방문한 node이므로 count를 하나 추가
            if i > max_distance:
                max_distance = i
                # 마지막 node에 닿는 순간이 다 방문하는 시간이므로 max_distance가 걸리는 시간
    print(count, max_distance)

    # A -> B, C로 간선이 2개라서 동시에 간다고 해서 
    # 그 시간을 각각 고려해야하는 것이 아니다.
    # 어차피 가장 오래걸리는 것이 기준임 (다익스트라 알고리즘의 특징)

'''

# 거의 최단경로 문제

from collections import deque
    # double-ended queue라서 왼쪽, 오른쪽에서 나 원소를 뽑을 수 있는 queue라고 보면 된다.
import heapq
import sys

input = sys.stdin.readline

def dijkstra():
    # 최단경로를 찾는 알고리즘
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

def bfs():
    # 최단경로를 end부터 역추적하는 알고리즘 
    q = deque()
    q.append(end)
    while q:
        now = q.popleft()
        if now == start:
            continue
        for prev, cost in reverse_adj[now]:
            if distance[now] == distance[prev] + cost:
                # 현재 node의 distance와 이전 node의 distance + cost와 동일하면
                # 이게 최단거리의 prev node
                dropped[prev][now] = True
                # 최단거리를 drop해야 하므로 prev와 now를 연결시키는 edge를 drop함
                # 이차원 리스트로 [from][to]를 체크하는 것임.
                q.append(prev)

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    reverse_adj = [[] for _ in range(n + 1)]
    # 역으로 거스르기 위해서 필요함
    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))
    dropped = [[False] * (n + 1) for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    dijkstra()
    bfs()
    distance = [1e9] * (n + 1)
    dijkstra()
    if distance[end] != 1e9:
        print(distance[end])
    else:
        print(-1)



