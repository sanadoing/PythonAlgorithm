from collections import deque

N = int(input())
cards = [(i + 1) for i in range(N)]
cards = deque(cards)
while len(cards) > 1:
    print(cards.popleft(), end=' ')
    cards.append(cards.popleft())
print(cards[0])
