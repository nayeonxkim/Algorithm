import sys
sys.stdin = open('input.txt')

lst = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())

    end = b - 1
    for i in range(a-1, (a+b)//2):
        lst[i], lst[end] = lst[end], lst[i]
        end -= 1

print(*lst)