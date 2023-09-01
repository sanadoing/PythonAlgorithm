import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    cards = []

    for _ in range(N):
        heapq.heappush(cards, int(input()))

    result = 0

    for i in range(N - 1):
        prev = heapq.heappop(cards)
        curr = heapq.heappop(cards)

        result += prev + curr
        heapq.heappush(cards, prev+curr)

    print(result)
