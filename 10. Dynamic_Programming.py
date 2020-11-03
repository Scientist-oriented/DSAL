# 피보나치 수열 구현하기

# recursive call을 활용하는 방법

def fibo(num):
    if num <= 1:
        return num
    
    return fibo(num-2) + fibo(num-1)

a = fibo(10)
print(a)

# Dynamic Programming을 활용하는 방법

def fibo_dp(num):
    cache = [0 for index in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index-1] + cache[index-2]

    return cache[num]

b = fibo_dp(9)
print(b)