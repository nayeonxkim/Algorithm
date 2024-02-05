import sys
sys.stdin = open('input.txt')
'''
0 1 2 3 4 5 6 7 

7 몇번?

1 -> 1
2 -> 1+1, 2 (2개)

3 -> 1 + 2, 2+1, 1+1+1 (3개)
4 -> 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2 (5개)
'''

N = int(input())
d = [0] * (N+1)
d[1] = 1
d[2] = 2

for i in range(3, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])