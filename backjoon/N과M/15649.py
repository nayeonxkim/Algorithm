import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def backtrack(i, N, M, lst):

    # 종료조건 1
    if len(lst) == M:
        print(*lst)
        return
        
    # 종료조건 2
    if i == N + 1:
        return

    # 재귀 호출
    backtrack(i + 1, N, M, lst + [i])
    backtrack(i + 1, N, M, lst)

backtrack(1, N, M, [])