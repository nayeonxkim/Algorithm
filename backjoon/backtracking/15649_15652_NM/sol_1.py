import sys
sys.stdin = open('input.txt')

def backtrack(N, M, lst):

    if len(lst) == M:
        print(*lst)
        return

    for n in range(1, N+1):
        if n not in lst:
            lst.append(n)
            backtrack(N, M, lst)
            lst.pop()


N, M = map(int, input().split())
backtrack(N, M, [])