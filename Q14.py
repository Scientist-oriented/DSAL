'''
# 바이러스 문제

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
k = int(input())

adjacent = [[] for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    adjacent[x].append(y)
    adjacent[y].append(x)

count = 0
visited = [False for _ in range(n+1)]

def dfs(v):
    global count
    count += 1
    visited[v] = True
    for e in adjacent[v]:
        if not visited[e]:
            dfs(e)  


dfs(1)
print(count - 1)

# 유기농 배추 문제

import sys
sys.stdin=open("input.txt", "rt")
sys.setrecursionlimit(100000)
    # 재귀함수의 깊이를 늘려준다.

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 탐색을 하기 위해서 연결가능 노드는 상하좌우라고 볼 수 있음.
        # 일단 연결가능한 노드를 모두 찾아보고 실제로 연결되어 있는지 반복문을 통해 접근
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx <0 or nx >= n or ny < 0 or ny >=m:
            # 밭 넓이 자체를 벗어나면 안됨
            continue
        if array[nx][ny] and not visited[nx][ny]:
            # 실제 배추가 있고 not visited라면
            # 탐색하러 감
            dfs(nx, ny)

for _ in range(int(input())):
    # test case가 나올 때는 이 방법을 활용해서 출력
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    # 이차원 배열 구현
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        # 이차원 배열해서는 array[y좌표][x좌표]로 구성이 되므로 바꾸어서 받아야
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                # 이 함수를 실행하면 연결된 것이 완전탐색됨.
                # 즉 result는 완전탐색이 한번 될 때마다 + 1씩 되는 것!
                result += 1
'''
# 효율적인 해킹
import sys
sys.stdin=open("input.txt", "rt")

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    count = 1
    # 한번만 탐색하는 것이 아니라 모든 컴퓨터에 대해 탐색해야하므로 visited를 함수 내부에 만든다
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
                # 탐색을 한번 할 때마다 count
                # dfs는 재귀함수라서 count를 외부에 만들어야하므로 bfs 활용
    return count

result = []
max_value = -1
    # max를 구할 때는 항상 가장 작은 값과 비교해서 실제값이 max에 저장될 수 있도록 해야한다.

for i in range(1, n + 1):
    # 컴퓨터마다 bfs 실행
    c = bfs(i)
    if c > max_value:
        # 저장된 최대값보다 더 큰 값이 나타나면
        result = [i]
        # result 갱신
        max_value = c
    elif c == max_value:
        # 최대값과 같은 값을 가진 컴퓨터가 나타나면
        result.append(i)
        # 결과에 추가
        max_value = c

for e in result:
    print(e, end=" ")

