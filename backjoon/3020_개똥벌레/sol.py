import sys
sys.stdin = open('input.txt')

N, H = map(int, input().split())
lst = [0] * H

for i in range(N):
    num = int(input())
    # 홀수면 위쪽에서부터
    if i % 2:
        for j in range(H-1, H-num-1, -1):
            lst[j] += 1

    # 짝수면 아래에서부터
    else:
        for j in range(num):
            lst[j] += 1

minV = min(lst)
minC = 0
for n in lst:
    if n == minV:
        minC += 1

print(minV, minC)