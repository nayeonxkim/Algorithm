import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 1. 버블정렬
for n in range(N-1, -1, -1):
    for i in range(n):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]


# 2. 이분 검색
def binary_search(lst, N, M):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == M:
            return mid + 1
        elif lst[mid] > M:
            end = mid - 1
        else:
            start = mid + 1
print(binary_search(lst, N, M))