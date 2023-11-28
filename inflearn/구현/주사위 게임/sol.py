import sys
sys.stdin = open('input.txt')

N = int(input())
max_ans = 0
for _ in range(N):
    lst = list(map(int, input().split()))

    if lst[0] == lst[1] == lst[2]:
        ans = lst[0] * 1000 + 10000
    elif lst[0] == lst[1]:
        ans = lst[0] * 100 + 1000
    elif lst[0] == lst[2]:
        ans = lst[0] * 100 + 1000
    elif lst[1] == lst[2]:
        ans = lst[1] * 100 + 1000
    else:
        ans = max(lst) * 100

    if ans > max_ans:
        max_ans = ans

print(max_ans)