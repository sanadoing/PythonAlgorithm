import heapq
n = int(input())
heap = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])