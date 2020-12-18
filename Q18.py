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

# 암호 만들기 문제

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

array = input().split(' ')
    # 여러 개가 들어오면 기본적으로 리스트로 저장
array.sort()
    # 사전식으로 출력해야 하므로 정렬을 수행

# 길이가 l인 모든 암호 조합을 확인
for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # password 안에 있는 모음의 개수를 센다.

    if count >= 1 and count <= l - 2:
        # 최소한 한개의 모음이 있는지
        # 그리고 l -2보다는 적게 모음이 있는지 (= 2개 이상의 자음이 있는지)
        print(''.join(password))
        # 리스트를 문자열로 합쳐주는 역할

# 암호 만들기 문제 (combination 함수 직접 만들기)

import copy

result = []
string = []
visited = []

def combination(array, length, index):
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return
    # 각 원소를 한 번씩만 뽑도록 구성
    for i in range(index, len(array)):
        if i in visited:
            continue
        string.append(array[i])
        visited.append(i)
        combination(array, length, i + 1)
        string.pop()
        visited.pop()

    # array = [0, 1, 2, 3, 4]
    # combination(array, 2, 0)으로 예를 들면
    # 일단 실행을 시키면 0번 인덱스로 시작하는 조합이 구해지기 위해서
        # combination(array, 2, 1)들이 돌기 시작함.
        # str은 [0]인 상태
    # 다시 1번 인엑스로 시작하는 조합이 구해지기 위해서
        # combination(array, 2, 2)들이 돌기 시작함.
        # str는 [1]인 상태

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

array = input().split()
array.sort()

combination(array, 1, 0)

for password in result:
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if count >= 1 and count <= l - 2:
        print(''.join(password))