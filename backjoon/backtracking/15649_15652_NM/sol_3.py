import sys
sys.stdin = open('input.txt')

def DFS(i, N, M, lst):
    lst.append(i)

    if len(lst) == M:
        print(*lst)
        return

    if i == N:
        return


    for n in range(1, N+1):
        lst.append(n)
        DFS(i+1, N, M, lst)
        lst.pop()



N, M = map(int, input().split())
DFS(1, N, M, [])