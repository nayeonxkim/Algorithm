import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
print(arr)

# 누적합 구하기 : O(N)
res = [0] * (N+1)
for i in range(N):
    res[i+1] = res[i] + arr[i]
print(res)


# 2개씩의 합 구하기 -> 리스트로 저장 : O(N)
# 한번 끌어진 차는 못끌고가
tot = []
for i in range(M, N+1):
    tot.append(res[i] - res[i-M])

# 인덱스+M이 진짜 인덱스
print(tot)

# visited 아닌 값중 최대값 찾는다.
# 해당 인덱스 i+M-t (t는 0, 1)를 visited표시한다.

visited = [0] * (N+1)
ans = 0
for _ in range(3):
    maxV = idx = 0
    for i in range(len(tot)):
        if maxV < tot[i] and not visited[i+M]:
            maxV = tot[i]
            idx = i
    ans += maxV
    for t in range(M):
        visited[idx + M - t] = 1
print(visited)


print(ans)
