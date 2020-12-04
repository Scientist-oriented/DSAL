# # 피보나치 수열
# import sys
# sys.stdin=open("input.txt", "rt")

# num = int(input())

# def fibo(n):
#     cache = [0 for _ in range(n+1)]
#     cache[0] = 0
#     cache[1] = 1

#     for index in range(2, n+1):
#         cache[index] = cache[index-1] + cache[index-2]
    
#     return cache[n]

# print(fibo(num))

# 0 만들기

import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        # deepcopy를 하는 이유는 id값을 다르게 하기 위해서
        # n queen 기본 예제에서 final_result[:]를 하는 이유와 동일
        return

    array.append(' ')
    recursive(array, n)
    # 이 함수를 return하는게 아니기 때문에
    # [' ']인 상태에서 이 함수를 다시 호출하고
    # 아래로 내려간다.
        # 즉 recursive에서 end조건에 걸리지 않는다면
        # 3가지 경우의 수를 만들고 종료되는 것임.
        # 즉 n인 경우 3^n 만큼의 경우의 수가 생기게 된다.
    array.pop()

    array.appen('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

