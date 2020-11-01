# 재귀함수

# 팩토리얼 구하는 알고리즘

def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1) # 굳이 else를 쓸 필요는 없음

def factorial2(num):
    if num > 1:
        return num * factorial2(num - 1)
    else:
        return num

a = factorial(4)
print(a)
b = factorial2(4)
print(b)

# 1부터 특정 숫자까지 곱하는 알고리즘

def multiply(num):
    if num <= 1:
        return num
    return num * multiply(num - 1)

a = multiply(10)
print(a)

# 리스트의 합을 구하는 알고리즘

list1 = [1,2,3,4,5]

def listsum(list):
    if len(list) <= 1:
        return list[0]
    return list[0] + listsum(list[1:]) # 슬라이싱을 활용

a = listsum(list1)
print(a)

# 특정 문자열이 회문인지 확인하는 알고리즘

def palindrome(string):
    if len(string) <= 0:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

a = palindrome("level")
b = palindrome("motor")

print(a, b)

# 프로그래밍 연습

def func(n):
    print(n)
    if n == 1:
        return
    
    if n % 2 == 0:
        return func(int(n / 2))
    else:
        return func (3 * n + 1)

func(3)

# 프로그래밍 연습 2

def func2(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2

    if n == 3:
        return 4

    return func2(n - 1) + func2(n - 2) + func2(n - 3)

a = func2(4)
b = func2(5)
print(a, b)


