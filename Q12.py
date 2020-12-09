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
'''
# 기타리스트 문제

import sys
sys.stdin=open("input.txt", "rt")

n, s, m = map(int, input().split())
array = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 일단 2차원 리스트 만들기
        # 가로축은 모든 볼륨 (0이면 재생불가, 1이면 재생가능)
        # y축은 음악재생횟수 (0번 ~ n번)
dp[0][s] = 1
    # 0번 재생했을 때 초기에 주어진 s 볼륨은 재생가능

for i in range(1, n + 1):
    # 각 재생횟수에 맞추어서
    for j in range(m + 1):
        if dp[i - 1][j] == 0:
            continue
        if j - array[i] >= 0:
            dp[i][j - array[i - 1]] = 1
        if j + array[i] <= m:
            dp[i][j + array[i - 1]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)