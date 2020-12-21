'''
# 피보나치 수열
import sys
sys.stdin=open("input.txt", "rt")

num = int(input())

def fibo(n):
    cache = [0 for _ in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, n+1):
        cache[index] = cache[index-1] + cache[index-2]
    
    return cache[n]

print(fibo(num))

# 0 만들기

import sys
sys.stdin=open("input.txt", "rt")

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

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)

    integers = [i for i in range(1, n + 1)]

    for operators in operators_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()

# 피보나치 수열 간단한 동적 계획법

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a+b
    n -= 1
    
print(a)
    # 최종으로 구하는 값만 필요한데 쓸 떼 없이 전부 저장할 필요는 없다.

'''
# Z 문제

import sys
sys.stdin=open("input.txt", "rt")

def solve(n, x, y):
    # 문제가 (x, y)로 주어지니까 변수도 마찬가지로 네모 안에 숫자 아니고
    # 좌표로 설정
    global result
        # result를 전역변수로 설정하여 recursive를 돌 때마다
        # 값이 누적되도록
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1

        if x == X and y == Y + 1:
            print(result)
            return
        result += 1

        if x == X + 1 and y == Y:
            print(result)
            return
        result += 1

        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
        # 이번 2*2 사각형에서 답을 못 찾았다면 그 함수는 종료시킨다.

    # 만약에 z를 하기에 너무 크다면 다시 4등분해서 각각 함수를 돌린다.
    solve(n / 2, x, y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)

result = 0
N, X, Y = map(int, input().split(' '))
solve (2 ** N, 0, 0)

