import sys
sys.stdin = open('input.txt')

def perm(num, N):

    res = ''
    for n in num:
        res += n

    for j in range(i, k):
        p[i], p[j] = p[j], p[i]
        perm(num, N-1)
        p[i], p[j] = p[j], p[i]

T = int(input())
for C in range(1, T+1):
    temp, N = input().split()
    num = list(temp)
    print(num)

    perm(num, N)
