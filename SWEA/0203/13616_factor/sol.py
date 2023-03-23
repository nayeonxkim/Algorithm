'''

2^^a X 3^^b X 5^^c X 7^^d X 11^^e
50 = 2 X 5^^2
50 // 2 = 25
25 //5 = 5
5 // 5 =1
2로 나누어 떨어지면 a+1
몫으로 업데이트



'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = b = c = d = e = 0

    while N > 1:
        if not (N % 2):
            a += 1
            N //= 2
        elif not (N % 3):
            b += 1
            N //= 3
        elif not (N % 5):
            c += 1
            N //= 5
        elif not (N % 7):
            d += 1
            N //= 7
        elif not (N % 11):
            e += 1
            N //= 11
    print(f'#{tc} {a} {b} {c} {d} {e}')