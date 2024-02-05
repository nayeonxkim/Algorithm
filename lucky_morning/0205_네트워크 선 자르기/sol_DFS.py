import sys
sys.stdin = open('input.txt')

'''
1m 자른 경우
2m 자른 경우
'''

cnt = 0
def DFS(N):

    global cnt

    if N < 0:
        return
    elif N == 0:
        cnt += 1
        return

    DFS(N-1)
    DFS(N-2)

N =  int(input())
DFS(N)
print(cnt)