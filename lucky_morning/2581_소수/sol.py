import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

sum = 0
min = N

for n in range(M, N+1):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        sum += n
        if i < min:
            min = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
