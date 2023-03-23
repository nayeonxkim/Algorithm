import sys
sys.stdin = open('input.txt')

def power(N, i, M, res):
    if i == M:
        print(res)
        return res

    power(N, i+1, M, res*N)

for _ in range(1, 11):
    tc = int(input())

    N, M = map(int, input().split())
    print(f'#{tc}', end = ' ')
    power(N, 1, M, N)


