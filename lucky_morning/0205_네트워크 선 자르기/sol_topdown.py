import sys
sys.stdin = open('input.txt')

def DFS(N):
    # N을 자르는 경우의 수를 이미 구했다면 바로 반환 -> 한번 구한 것에 대해 다시 진행 X
    if d[N] > 0:
        return d[N]
    
    # N이 1이라면 1가지, 2라면 2가지 경우가 있음
    if N == 1 or N == 2:
        return N
    # 3이상이라면 -1, -2한 값의 자르는 경우의 수를 더한 값이 현재 길이를 자르는 경우의 수
    else:
        d[N] = DFS(N-1) + DFS(N-2)
        return d[N]


N = int(input())
d = [0] * (N+1)
print(DFS(N))