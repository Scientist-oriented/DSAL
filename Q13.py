'''
# BFS, DFS
import sys
sys.stdin=open("input.txt", "rt")

from collections import defaultdict
n, m, v = map(int, input().split(' '))
graph = defaultdict(list)

for i in range(n):
    v, u = map(int, input().split(' '))
    graph[v].append(u)
    graph[u].append(v)

for key in graph:
    graph[key].sort()
    

def bfs(graph, start):
    need_visit = list()
    visited = list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited



def dfs(graph, start):
    need_visit = list()
    visited = list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

a = bfs(graph, 1)
print(a)
b = dfs(graph, 1)
print(b)

# BFS, DFS 모범답안

from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)
        # adj부터 탐색하게 되므로 자식 node 먼저 감
        # recursive라서 자식node부터 쭉 내려가고 나서 다른 adjacent 확인

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        # queue를 만들어 놓고 FIFO 방식으로 하니까 형제 node 우선
        if not (visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
    # 인덱스 번호랑 node 번호랑 맞추기 위해서 n + 1개 만듬

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()
    # 이렇게 하면 방문하는 node가 여러개 일때 순서대로 방문할 수 있음.

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
'''
# 숨바꼭질
    # 주어진 그래프가 없어도 완전탐색의 원리를 활용해서 갈 수 있는 경우의 수를 모두 탐색하는 방법

from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX
    # 그 지점까지 가는데 걸리는 시간을 모두 저장하기 위해서 리스트를 만든다.

def bfs():
    q = deque([n])
    # 시작지점을 queue에 넣고
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
            # 동생의 위치가 나오면 return
        for next_pos in (now_pos - 1, now_pos + 1, 2 * now_pos):
            # 이동으로 갈 수 있는 3갈래 길을 구하고
            if 0 <= next_pos < MAX and not array[next_pos]:
                # 갈 수 없는 위치이거나 이미 왔던 곳 (표준 bfs에서 visited에 속하는 경우/왜냐면 이미 왔던 곳은 더 빨리오는 방법이 존재하기 때문에)를 제외하고
                array[next_pos] = array[now_pos] + 1
                # 그 전 위치의 시간값에 1을 추가하고
                q.append(next_pos)
                # queue에 넣음
