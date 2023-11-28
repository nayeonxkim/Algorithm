import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))

tot = 0
now = 0
for i in lst:
    if i == 1:
        now += 1
        tot += now
    else:
        now = 0

print(tot)