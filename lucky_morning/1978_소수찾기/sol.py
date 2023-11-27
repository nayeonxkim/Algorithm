import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int,input().split()))

cnt = 0
for num in numbers:
    i_num = 0
    for i in range(1, num+1):
        if num % i == 0:
            i_num += 1
    if i_num == 2:
        cnt += 1
print(cnt)