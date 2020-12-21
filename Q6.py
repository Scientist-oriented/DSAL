'''
# 수 정렬하기 2

import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)
'''

# K번째 수

import sys
sys.stdin=open("input.txt", "rt")

N, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

nums.sort()

print(nums[K - 1])