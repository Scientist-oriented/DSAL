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