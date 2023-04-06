import sys
sys.stdin = open('../15650_NM2/input.txt')

def DFS(i, N, M, lst):

    # 백트래킹
    if len(lst) == M:
        print(*lst)
        return

    # 종료조건
    # i == 4인 경우까지는 호출되어야함.
    # 따라서 i가 5가 된 경우에는 재귀호출을 멈춘다.
    if i == N+1:
        return

    # i를 포함한 경우와 포함하지 않은 경우를 각각 호출
    DFS(i+1, N, M, lst + [i])
    DFS(i+1, N, M, lst)

N, M = map(int, input().split())
DFS(1,N,M,[])