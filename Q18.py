# n queen 문제

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)
                # 여기는 list에 저장하는 것이 없으므로 pop 같은거 없어도 된다.

n = int(input())
row = [0] * n
    # 각 row 별로 어느 column에 위치해있는지 기록하는 역할
result = 0
dfs(0)
print(result)


# 알파벳 문제

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    # 좌표의 이동
    # 각 인덱스별로 좌, 우, 하, 상으로 이동

def bfs(x, y):
    global result
    q = set()
    # 중복은 1회만 계산하기 위해서 set 사용
    q.add((x, y, array[x][y]))

    while q:
        x, y, step = q.pop()
        # 스텝에는 지금까지 지나온 알파벳이 str형태로 들어있음.
        result = max(result, len(step))
        # result step의 길이와 비교해서 계속 업데이트 해나감

        for i in range(4):
            # 상하좌우 모든 방향을 고려
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx and nx < r and 0 <= ny and ny < c and array[nx][ny] not in step):
                # 이동한 점이 보드를 벗어나지 않고 지금까지 지나온 알파벳이 아닌 경우
                q.add((nx, ny, step + array[nx][ny]))

r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(input())
    # str와 리스트로 이루어진 2차원 리스트로 array를 구성

result = 0
bfs(0, 0)
print(result)