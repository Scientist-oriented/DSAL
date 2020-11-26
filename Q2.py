# 수열
'''
import sys
sys.stdin=open("input.txt", "rt")

total = int(input())
stack = []
result = []
count = 0

for _ in range(total):
    stand = int(input())
    while count < stand:
        count += 1
        stack.append(count)
        result.append("+")
    if stack[-1] == stand:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print('\n'.join(result))

# 수열 모범답안

n = int(input())
count = 1
stack = []
result = []
for i in range(1, n + 1): # 데이터 개수만큼 반복
    data = int(input())
    while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('NO')
        exit(0)
print('\n'.join(result)) # 가능한 경우

# 프린터큐

import sys
sys.stdin=open("input.txt", "rt")

result = []

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    pre_queue = list(map(int, input().split()))
    queue = [(i, pre_queue[i]) for i in range(len(pre_queue))]
    pre_queue.sort(reverse=True)
    print_count = 0

    while True:
        if queue[0][1] != pre_queue[0]:
            queue.append(queue[0])
            del queue[0]
        else:
            if queue[0][0] == m:
                print_count += 1
                result.append(print_count)
                break
            else:
                print_count += 1
                del queue[0]
                del pre_queue[0]

result = [str(result[i]) for i in range(test_case)]
print('\n'.join(result))

# 프린터 모범답안

import sys
sys.stdin=open("input.txt", "rt")

test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)] # 리스트의 원소를 index와 함께 튜플로 저장
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0) # 찾는게 아니면 그냥 queue에서만 제거하면 됨
        else:
            queue.append(queue.pop(0)) # pop한 후에 바로 append

# 키로거 문제

import sys
sys.stdin=open("input.txt", "rt")

test_case = int(input())

for _ in range(test_case):
    string = str(input())
    cursor_position = 0
    result = str()
    for index in range(len(string)):
        if string[index] == "<":
            if cursor_position > 0:
                cursor_position -= 1
        elif string[index] == ">":
            if cursor_position < len(result):
                cursor_position += 1
        elif string[index] == "-":
            if cursor_position > 0:
                # result = result.replace(result[cursor_position - 1], "", 1) # replace는 모든 겹치는 글자를 다 없앤다!!! (= JS의 replace ALL)
                left, temp, right = result[:cursor_position-1], result[cursor_position - 1], result[cursor_position:]
                result = left + right
                cursor_position -= 1
        else:
            result = result[:cursor_position] + string[index] + result[cursor_position:]
            cursor_position += 1
    print(result)

# 답은 나오는 문제였지만 시간복잡도 때문에 시간초과가 나옴

# 키로거 문제 모범답안

# 문자열의 크기가 최대 100만이므로 시뮬레이션 방식으로는 불가능
# 그래서 스택을 활용하여 풀음
# 문제를 그대로 옮기는 것이 시뮬레이션
    # 하지만 100만 이상은 그대로 하면 안되고 최대한 시간을 절약할 수 있는 방법을 고안해야 한다!

import sys
sys.stdin=open("input.txt", "rt")

test_case = int(input())
for _ in range(test_case):
    left_stack = []
    right_stack = []
    data = input()
    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

'''

