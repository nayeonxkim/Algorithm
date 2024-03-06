import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 1. 정렬
lst.sort()

# 2. 이분탐색
s = 0
e = N-1

while s <= e:
    mid = (s+e) // 2

    if lst[mid] == M:
        print(mid+1)
        break

    elif lst[mid] > M:
        e = mid - 1

    else:
        s = mid + 1

