import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    boong = [0] * (customer[-1] + 1)

    # M초에 K개씩 붕어빵 생성
    for i in range(0, len(boong), M):
        boong[i] = K
    boong[0] = 0

    # 누적 붕어빵 개수
    for i in range(1, len(boong)):
        boong[i] += boong[i-1]

    # 손님에게 붕어빵 제공
    ans = 'Possible'
    for n in customer:
        for i in range(n, len(boong)):
            boong[i] -= 1
        if boong[n] < 0:
            ans = 'Impossible'

    print(f'#{tc} {ans}')