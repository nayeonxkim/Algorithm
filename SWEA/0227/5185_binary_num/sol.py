import sys
sys.stdin = open('input.txt')

asc = {hex(i).replace('0x', '') : f'{i:04b}' for i in range(16)}
print(asc)
T = int(input())
for tc in range(1, T+1):
    N, num_16 = input().split()
    N = int(N)
    num_16 = num_16.lower()
