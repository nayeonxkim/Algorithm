import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    i = ans = 0
    while i < N:
        # i부터 끝까지 최대값의 인덱스 찾기
        i_mx = i
        for j in range(i+1, N):
            if price[i_mx] < price[j]:
                i_mx = j

        # i부터 i_mx까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += price[i_mx] - price[j]

        i = i_mx + 1
    print(ans)