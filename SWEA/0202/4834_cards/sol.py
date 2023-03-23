import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = int(input())

    # cnt 배열 생성 및 숫자별 개수 대입
    cnt = [0] * 10
    for n in range(N):
        cnt[card % 10] += 1
        card //= 10

    # 가장
   maxC = 0
    for i in range(10):
        if maxC <= cnt[i]:
            maxC = cnt[i]
            idx = i

    print(f'#{tc} {idx} {maxC}')
