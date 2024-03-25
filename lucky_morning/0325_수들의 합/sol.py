import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0

for i in range(N):
    tot = lst[i]
    for j in range(i+1, N):
        tot += lst[j]
        if tot == M:
            cnt += 1
            break

print(cnt)



# cnt = 0
# def DFS(i, lst, tot):
#     global cnt
#
#     if tot == M:
#         cnt += 1
#         return
#
#     if i >= N:
#         return
#
#     if tot > M:
#         return
#
#     DFS(i+1, lst, tot+lst[i])
#
# for i in range(N):
#     DFS(i, lst, 0)

# print(cnt)
