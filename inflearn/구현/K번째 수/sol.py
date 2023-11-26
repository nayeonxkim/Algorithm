import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers[s-1:e])
    print(f'#{t} {numbers[k-1]}')