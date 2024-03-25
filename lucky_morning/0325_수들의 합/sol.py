import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
lst = list(map(int, input().split()))

s = 0
e = 1
cnt = 0

while s <= N and e <= N:
    tot = sum(lst[s:e])
    if tot == M:
        cnt += 1
        e += 1

    elif tot < M:
        e += 1

    else:
        s += 1

print(cnt)