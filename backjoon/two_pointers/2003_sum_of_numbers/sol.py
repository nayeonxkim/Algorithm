import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# two pointers = start, end
# 처음엔 start, end 모두 0에서 시작
start = 0
end = 0

cnt = 0
while start < N and end < N:

    new_arr = arr[start:end+1]
    tot = sum(new_arr)

    if tot == M:
        cnt += 1
        start += 1

    elif tot < M:
        end += 1

    else:
        start += 1

print(cnt)

