import sys
sys.stdin = open('input.txt')

lst = list(range(1, 21))

for _ in range(10):
    s, e = map(int, input().split())
    lst[s-1:e] = reversed(lst[s-1:e])

print(*lst)