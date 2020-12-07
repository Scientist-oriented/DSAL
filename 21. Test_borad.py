import heapq

heap = []

heapq.heappush(heap, 1)
heapq.heappush(heap, 6)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 7)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))