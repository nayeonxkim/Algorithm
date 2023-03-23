'''
111456

cnt
[0, 3, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]

triplet 조사
for i in range(10)
    cnt[i] 3이상이면
        cnt[i] -3,
        tri += 1
        그리고 처음부터
    cnt[i] + cnt[i+1] + cnt[i+2]가 3이상이면
        cnt[i], cnt[i+1], cnt[i+2] -1
        run += 1
        그리고 처음부터

## while 쓰는 이유 : for문 돌리면 무조건 i=1 다음 i=2 넘어감
while문은 i에 1을 더해주지 않으면 다음 인덱스로 넘어가지 않음
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    numbers = int(input())

    ## 카운트 배열 생성
    # triplet과 run을 한 반복문에서 계산하기 위해 10개가 아닌 12개로 만든다.
    # : run은 세개씩 묶음으로 확인하기 때문
    cnt = [0] * 12
    for i in range(6):
        cnt[numbers % 10] += 1
        numbers //= 10

    ## triplet부터 확인
    # cnt가 3이상이면 -3, triplet+1
    # 해당 인덱스가 3미만일 때까지 다시 확인
    # : 만약 cnt[i] = 6이라면 두 번 확인해야하기 올바른 결과가 나오기 때문.

    ## run확인
    # 연달아 세 개가 모두 1이상이면 각각 -1, run+1
    # 해당 인덱스들이 1미만일 때까지 다시 확인
    i = 0
    triplet = run = 0
    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            triplet += 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            run += 1
            continue
        i += 1

    # triplet과 run을 합쳐 2 => baby-gin
    if triplet + run == 2:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')

