import sys
sys.stdin = open('input.txt')

# N, H = map(int, sys.stdin.readline().split())
#
# upper = [0] * N
# lower = [0] * N
#
# for _ in range(N//2):
#     l = int(sys.stdin.readline())
#     u = int(sys.stdin.readline())
#     lower[l] = upper[u] = 1
#
# print(lower, upper)


N, H = map(int, sys.stdin.readline().split())
lst = [0] * H

for _ in range(N//2):
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())

    for i in range(H-1, H-A-1, -1):
        lst[i] += 1

    for i in range(B):
        lst[i] += 1
print(lst)
minV = min(lst)
print(minV, lst.count(minV))
