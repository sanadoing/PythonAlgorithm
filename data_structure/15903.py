import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
result = 0

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    heapq.heappush(cards, x + y)
    heapq.heappush(cards, x + y)

result = sum(cards)
print(result)
