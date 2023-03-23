import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = [0] * 10001
for _ in range(N):
    i = int(input())
    cnt[i] += 1

for i in range(10001):
    if cnt[i] == 0:
        continue
    for _ in range(cnt[i]):
        print(i)