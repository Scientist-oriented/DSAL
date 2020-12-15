# n queen 문제

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)
                # 여기는 list에 저장하는 것이 없으므로 pop 같은거 없어도 된다.

n = int(input())
row = [0] * n
    # 각 row 별로 어느 column에 위치해있는지 기록하는 역할
result = 0
dfs(0)
print(result)


