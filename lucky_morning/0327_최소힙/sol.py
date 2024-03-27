import sys
sys.stdin = open('input.txt')
import heapq

heap = []

while True:
    N = int(input())
    if N == 0:
        if not heap:
            print(-1)
        else:
            print(heapq.heappop(heap))
    elif N == -1:
        break
    else:
        heapq.heappush(heap, N)

