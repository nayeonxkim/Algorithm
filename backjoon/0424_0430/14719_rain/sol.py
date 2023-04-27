import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
arr = list(map(int, input().split()))

# 최대값 기준으로 좌우 나눔
max_idx = 0
for i in range(1, W):
    if arr[max_idx] <= arr[i]:
        max_idx = i

if max_idx in (0, W):
    left = arr
    right = []
else:
    left = arr[:max_idx+1]
    right = arr[max_idx:]

# 왼쪽은 0번 부터
res = 0
for i in range(len(left)-1):
    for j in range(i+1, len(left)):
        if left[i] > left[j]:
            res += left[i] - left[j]
            left[j] = left[i]
        else:
            break

# 오른쪽은 마지막 부터
for i in range(len(right)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if right[i] > right[j]:
            res += right[i] - right[j]
            right[j] = right[i]
        else:
            break
print(res)