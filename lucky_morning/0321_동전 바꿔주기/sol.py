import sys
sys.stdin = open('input.txt')

T = int(input())
k = int(input())
inp = [list(map(int, input().split())) for _ in range(k)]

cnt = 0

lst = []
for l in inp:
    for i in range(l[1]):
        lst.append(l[0])
print(lst)

res = []
def DFS(i, lst, T, now):
    global res

    if i >= len(lst):
        return

    if sum(now) > T:
        return

    if T == sum(now):
        if now not in res:
            res.append(now)

        return

    DFS(i+1, lst, T, now + [lst[i]])
    DFS(i+1, lst, T, now)


DFS(0, lst, T, [])
print(res)