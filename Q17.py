# 센서
import sys

n = int(input())
k = int(input())

# 집중국의 개수가 센서보다 많거나 같을 때
    # 이러한 예외처리를 잘 할 수 있어야 함!
if k >= n:
    print(0)
    sys.exit()
    # 센서의 위치마다 설치하면 된다.

# 모든 센서의 위치를 입력 받아 오름차순 정렬
array = list(map(int, input().split()))
array.sort()

# 각 센서 사이의 거리를 계산하여 내림차순으로 정렬
distance = []
for i in range(1, n):
    distance.append(array[i] - array[i - 1])
distance.sort(reverse=True)

# 가장 긴 거리부터 하나식 제거
    # 집중국이 하나 생길 때마다 센서 사이의 거리 하나씩 상쇄
    # 최소가 되야하는 것이 집중국-센서 사이의 거리가 아니고
    # 수신가능영역의 길이 (센서-센서 사이의 거리)임.
    # 따라서 집중국이 어디에 세워질지는 애초에 고려의 대상이 아니다.
for i in range(k - 1):
    distance[i] = 0

print(sum(distance))

# 도서관 문제
    # 음수와 양수를 구분해서 써야함!
        # 왜냐면 음수와 양수를 묶게 되면 어차피 0을 지나가게 되므로
    # 그리고 원래 위치로 돌아올 필요가 없으므로 가장 먼 거리에 있는 책은 편도로 한번만 가는 것이 효과적!

import heapq

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

# 가장 먼 거리의 책은 미리 빼놓는다.
largest = max(max(array), -min(array))
    # 절대값이 가장 큰 양수와 음수의 절대값을 비교

# heapq라이브러리는 최소힙 (Min Heap)이기 때문에 원소를 음수로 구성
    # Max Heap으로 만들기 위해서
        # 그래야지 절대값이 큰(= 거리가 먼) 책부터 pop됨
    # 멀리 있는 책부터 m개 묶어야함!
        # 왜냐하면 그래야지 먼 책을 옮길 때 약간 덜 먼책이 묻어갈 수 있기 때문

for i in array:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0

while positive:
    result += heapq.heappop(positive)
    # 가장 거리가 먼 것 기준으로 결과에 추가
        # 나머지는 가는 도중에 제 자리에 둘 수 있으므로
    for _ in range(m -1):
        if positive:
            heapq.heappop(positive)
            # 한번에 가지고 갈 수 있는 m가 pop (맨처음에 result에서 하나 뺏으므로 m - 1)
            # heap에 m -1개 보다 적게 남아있어도 상관없음 (어차피 result에 영향을 주지 않으므로)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - largest)
    # largest는 편도로 갈 것이기 때문에 한번 빼줌

# 컵라면 문제

import heapq

n = int(input())
array = []
q = []

# 문제를 데드라인 순으로 정렬
for i in range(n):
    a, b = map(int, input().split(' '))
    array.append((a, b))
array.sort()
    # 몇번 문제를 풀고 이런 정보는 저장할 필요가 없음.

for i in array:
    a = i[0]
    heapq.heappush(q, i[1])
    # q에 넣으면 문제를 푼 것임. (상품인 컵라면만 저장)
    # 즉 q의 길이는 문제를 푼 시간(초)에 해당한다.
    if a < len(q):
        heapq.heappop(q)
        # 그런데 만약에 데드라인이 문제를 푼 시간보다 짧다면 (즉 시간초과)
        # 그렇다면 문제를 pop한다.
            # 이 때 q를 최소힙으로 쓴 이유는 같은 데드라인을 초과해서 문제를 풀게 될 경우
            # 보상을 조금 주는 문제가 pop해야 하므로! (데드라인이 짧더라도 보상이 적으면 pop된다.)

print(sum(q))