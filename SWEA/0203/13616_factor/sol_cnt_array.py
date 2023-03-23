import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    divs = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    # 0, 1, 2, 3, 4 -> 2, 3, 5, 7, 11
    for i in range(len(divs)):
        while not (N % divs[i]):
            cnt[i] += 1
            N //= divs[i]
    print(f'#{tc}', *cnt)

