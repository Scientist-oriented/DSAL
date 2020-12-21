'''
# 01 타일 문제
    # 단순하게 무조건 계산해보고 하는 것이 아니라
    # 점화식을 수학적으로 세워야함. (동적프로그래밍의 핵심 = 점화식)
    # 프린트물 참고

n = int(input())

results = [0] * 1000001
    # 시간을 절약하기 위해서 반복문을 도는게 아니라 미리 최대값만큼 만들어 놓는다.

results[1] = 1
results[2] = 2

for index in range(3, n + 1):
    results[index] = (results[index - 2] + results[index - 1]) % 15746
    # 메모리 절약을 위해서 큰수가 저장되지 않게 미리 나눈다.
    # 나머지끼리 더해서 나눈 나머지 = 다 더해서 나눈 나머지

print(results[n])

# 평범한 배낭문제
    # 복잡한 문제임! 차분하게 생각할 것!

import sys
sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
    # 2차원 리스트
    # 각각 짐을 입력받을 때마다 한줄한줄 갱신함
    # 가방의 무게에 따라서 최대값을 구해야함.
    # 즉 x축의 값들은 가방의 무게
        # 그래서 아래로 내려가면서 그 무게에 따른 value들을 갱신해나가는 것임.
        # 그래서 마지막에 dp[n][k]를 구하면 최대값이 나오는 것!

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
            # 만약에 짐이 들어갈 수 없다면 바로 전에 입력한 값이 넣을 수 있는 짐의 최댓값 (값을 그대로 이어받음.)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            # 만약에 짐이 들어갈 수 있는 크기라면?
            # 원래의 최댓값과
            # 그 짐을 넣을 수 있는 공간을 확보하고 그 짐의 가치만큼 값을 더해서
            # 두 값을 비교하여 최댓값을 구함

print(dp[n][k])
'''
# 가장 긴 증가하는 부분 수열

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    # 0은 어차피 1이므로 고려할 필요는 없음.
    for j in range(0, i):
        # 기준을 array[i]로 잡고 그 아래의 수들을 확인
        if array[j] < array[i]:
            # 그 아래에 더 작은 수가 있다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 원래 수열하고 거기서 부터 array[i]로 이어지는 수열과 비교
            # 계속 갱신해가면서 최장수열을 구하는 시스템

print(max(dp))


            