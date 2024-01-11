import sys
sys.stdin = open('input.txt')


'''
100보다 작은 모든 A, B에 대해
A*B가 A,B의 문자로만 이루어졌는지 확인하기
'''
N, M = map(int, input().split())
cnt = 0
for a in range(1, N+1):
    for b in range(1, M+1):
        c = a * b
        for char in str(c):
            if char in str(a) + str(b):
                cnt += 1

print(cnt)