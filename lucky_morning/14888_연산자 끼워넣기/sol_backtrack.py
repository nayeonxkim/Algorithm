from itertools import permutations
import sys

sys.stdin = open('input.txt')

# 1. 입력받기
N = int(input())
lst = list(map(int, input().split()))
p, m, mt, dv = map(int, input().split())

# 2. 초기 최대/최소값 설정
maxV = 0
minV = 100 * 11

# 3. 백트래킹
def backtrack(lst, i, res):
    global p, m, mt, dv

    if i >= N:
        return res


    if p:
        p -= 1
        backtrack(lst, i+1, res+lst[i])
        p += 1
    if m:
        m -= 1
        backtrack(lst, i+1, res-lst[i])
        m += 1
    if mt:
        mt -= 1
        backtrack(lst, i+1, res*lst[i])
        mt += 1
    if dv:
        dv -= 1
        if res < 0:
            backtrack(lst, i+1, -(abs(res)//lst[i]))
        else:
            backtrack(lst, i+1, res//lst[i])
        dv += 1
print(backtrack(lst, 0, 0))