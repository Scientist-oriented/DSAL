'''
# 최소힙 문제

import sys
sys.stdin=open("input.txt", "rt")

class Heap:
    def __init__(self):
        self.heap_array = list()
        self.heap_array.append(None)

    def insert(self, data):
        self.heap_array.append(data)

        inserted_index = len(self.heap_array) - 1

        while self.move_up(inserted_index):
            parent_index = inserted_index // 2
            if self.heap_array[parent_index] > self.heap_array[inserted_index]:
                self.heap_array[parent_index], self.heap_array[inserted_index] = self.heap_array[inserted_index], self.heap_array[parent_index]
                inserted_index = parent_index

    def move_up(self, inserted_index):
        if inserted_index <= 1:
            return False
        parent_index = inserted_index // 2
        if self.heap_array[parent_index] > self.heap_array[inserted_index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:
            print(0)
            return

        returned_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        del self.heap_array[-1]

        popped_index = 1

        while self.move_down(popped_index):
            left_child_index = 2 * popped_index
            right_child_index = 2 * popped_index + 1
        
            if right_child_index > len(self.heap_array) - 1:
                if self.heap_array[left_child_index] < self.heap_array[popped_index]:
                    self.heap_array[left_child_index], self.heap_array[popped_index] = self.heap_array[popped_index], self.heap_array[left_child_index]
                    popped_index = left_child_index
            else:
                if self.heap_array[left_child_index] < self.heap_array[right_child_index]:
                    self.heap_array[left_child_index], self.heap_array[popped_index] = self.heap_array[popped_index], self.heap_array[left_child_index]
                    popped_index = left_child_index
                else:
                    self.heap_array[right_child_index], self.heap_array[popped_index] = self.heap_array[popped_index], self.heap_array[right_child_index]
                    popped_index = right_child_index
                  
        print(returned_data)

    def move_down(self, popped_index):
        left_child_index = 2 * popped_index
        right_child_index = 2 * popped_index + 1

        if left_child_index > len(self.heap_array) - 1:
            return False
        elif right_child_index > len(self.heap_array) - 1:
            if self.heap_array[left_child_index] < self.heap_array[popped_index]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_index] < self.heap_array[right_child_index]:
                if self.heap_array[left_child_index] < self.heap_array[popped_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_index] < self.heap_array[popped_index]:
                    return True
                else:
                    return False


n = int(input())

heap = Heap()

for _ in range(n):
    case = int(input())
    if case <= 0:
        heap.pop()
    else:
        heap.insert(case)


# 카드 정렬하기 문제

import sys
sys.stdin=open("input.txt", "rt")

import heapq

heap = []
result = 0

n = int(input())

for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a + b
    heapq.heappush(heap, a + b)
    # 합쳐진 카드뭉치가 다시 heap으로 들어간다는 생각을 했어야함!!!

print(result)
'''
# 문제집 문제 (위상정렬)
    # 순서가 정해진 작업을 차례로 수행해야할 때
    # 위상정렬은 사이클이 없음

import sys
sys.stdin=open("input.txt", "rt")

import heapq

n, m = map(int, input().split())
array = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)
    # 진입차수를 저장함 (이 node에 진입하기 위해서 얼마의 node를 진입해서 들어와야하는가?)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] == 0:
            # 진입차수가 0이면 우선순위큐에 등록
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')
    
                


