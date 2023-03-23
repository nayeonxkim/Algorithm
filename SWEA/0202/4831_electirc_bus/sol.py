'''
3, 10, 5

0~10까지 이동
- 배열 = [0] * 10

충전정류장 : 5군데
- 배열에서 해당 인덱스 5개의 값 = 최대 이동 정류장 수 3
[3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]

최대 이동정류장수 : 3개
[3, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]

arr[i] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
10-i   = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
누적 cnt =[3, 5, 4, 6, 5, 7, 6, 5, 4, 3, 2 ]

arr[i] >= 10-i: [i]-1만
[i]-1, [i+1]
---
누적 cnt

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))

    # 정류장 표시 : 충전 정류장 = 최대 이동정류장 수
    arr = [0] * (N+1)
    arr[0] = K
    for i in charge_stop:
        arr[i] += K

    # 끝까지 남은 수보다
    charge = 0
    for i in range(1, N+1):
        if arr[i-1] > N-(i-1)-1:
            arr[i] = arr[i-1] - 1
        else:
            arr[i] = arr[i-1] - 1 + arr[i]


    if arr[-1] < 0:
        ans = 0
    else:
        ans = charge
    print(f'#{tc} {ans}')
    print(arr)


