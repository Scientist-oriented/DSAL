'''
# LCS 문제

x = input()
y = input()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    # 이차원 리스트는 수열보다 하나 길게 만들자

for i in range(1, len(x) + 1):
    # x 수열의 요소 하나하나를
    for j in range(1, len(y) + 1):
    # y 수열 전체와 비교하는 과정
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            # 동일한게 있다면? 그 이전까지의 수열과 이전까지의 문자를 비교한 결과에 +1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            # 동일한게 없다면
            # x 와 y - 1의 수열과 x - 1, y 의 수열 중에 긴 것을 채택함.

print(dp[len(x)][len(y)])

# 기타리스트 문제

import sys
sys.stdin=open("input.txt", "rt")

n, s, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 일단 2차원 리스트 만들기
        # 가로축은 모든 볼륨 (0이면 재생불가, 1이면 재생가능)
        # y축은 음악재생횟수 (0번 ~ n번)
        # 모두 일단 0(False)로 맞추어 놓음
dp[0][s] = 1
    # 0번 재생했을 때 초기에 주어진 s 볼륨은 재생가능

for i in range(1, n + 1):
    # 각 재생횟수에 맞추어서
    # i가 바뀌면 일단 값들은 모두 False인 상황
    # 어차피 dp는 중간단계는 의미없고 마지막 줄만 활용하는 것임!!!
    for j in range(m + 1):
        if dp[i - 1][j] == 0:
            continue
            # 만약에 그 전단계에서 False인 볼륨이면 여기에서 따질 필요 없음

        # 그 전단계에서 True인 볼륨이라면 continue에 걸리지 않고 아래로 내려옴    
        if j - array[i - 1] >= 0:            
            dp[i][j - array[i - 1]] = 1
            # 볼륨 전환을 계산해보고 가능하면 True로 저장함.
        if j + array[i - 1] <= m:
            dp[i][j + array[i - 1]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
    # 최대볼륨을 구하기 위해 최대볼륨부터 True인 볼륨을 완전탐색함.

print(result)


# 가장 높은 탑 쌓기

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
bricks = []
dp = [1] * n

for index in range(n):
    size, height, weight = map(int, input().split())
    bricks.append((index, size, height, weight))

bricks = sorted(bricks, key=lambda x: x[3])

for i in range(1, n):
    for j in range(0, i):
        if bricks[j][1] < bricks[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

max_tower = 0
last_brick = 0

for index in range(n):
    if dp[index] > max_tower:
        max_tower = dp[index]
        last_brick = bricks[index]

max_tower_bricks = [last_brick]
now = max_tower_bricks[0]

for index in range(len(bricks) - 1, -1, -1):
    if bricks[index][1] < now[1] and bricks[index][3] < now[3]:
        max_tower_bricks.append(bricks[index])
        now = bricks[index]

print(max_tower)
max_tower_bricks.reverse()
for brick in max_tower_bricks:
    print(brick[0] + 1)

'''


