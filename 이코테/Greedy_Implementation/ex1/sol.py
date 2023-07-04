'''
K로 나누기, 1 빼기 -> 1이 되는 최소 횟수
'''

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

cnt = 0
while N != 1:
    # 나누어 떨어지는지 확인
    nn = N % K
    if N == 2:
        cnt += 1
        N -= 1
    elif nn:
        cnt += nn
        N -= nn
    else:
        cnt += 1
        N //= K

print(cnt)

