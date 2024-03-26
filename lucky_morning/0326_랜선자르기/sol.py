import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())
lst = list(int(input()) for _ in range(K))

s = 0
e = max(lst)
maxM = 0

while s <= e:
    mid = (s+e) // 2
    cnt = 0

    for l in lst:
        cnt += (l // mid)

    if cnt >= N:
        maxM = max(maxM, mid)
        s = mid + 1

    else:
        e = mid - 1

print(maxM)
