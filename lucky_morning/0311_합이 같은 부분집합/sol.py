import sys
sys.stdin = open('input.txt')

def DFS(i, total):
    global result

    if total > sum(lst)//2:
        return

    if i == N:
        if total == (sum(lst) - total):
            result = 'YES'
            return

    else:
        DFS(i+1, total+lst[i])
        DFS(i+1, total)


N = int(input())
lst = list(map(int, input().split()))
result = 'NO'
DFS(0, 0)
print(result)