import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[1])


cnt = 0
for p1 in arr:
    for p2 in arr:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            break
    else:
        cnt += 1

print(cnt)