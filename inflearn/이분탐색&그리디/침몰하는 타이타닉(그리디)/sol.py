from collections import deque
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 리스트 오름차순 정렬 및 데큐 변환
arr.sort()
arr = deque(arr)

# 2. 마지막 + 첫번째의 합을 기준으로 보트 수 +
cnt = 0
while arr:
    if arr[0] + arr[-1] > M:
        arr.pop()

    else:
        arr.popleft()
        arr.pop()
    cnt += 1
print(cnt)