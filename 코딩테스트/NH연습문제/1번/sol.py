import sys
sys.stdin = open('input.txt')

n, r = map(int, input().split())
res = n * (r/100)
print(int(res))