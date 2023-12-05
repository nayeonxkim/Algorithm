'''
1 ~ 802 이분 탐색
1) 401
- 401로 리스트의 모든 숫자를 나눔
- 몫들을 더함
- N개 보다 적음 -> 길이를 더 줄여야함 -> end = mid - 1

1 ~ 400 이분 탐색
2) 200
- 200으로 리스트의 모든 숫자를 나눔
- 몫들을 더함
- N개보다 크거나 같음 -> 최대 mid 업데이트 + 더 긴 mid가 있을 수 있으므로 길이를 늘려봐야함
-> start = mid + 1

'''

import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())
lst = list(int(input()) for _ in range(K))

def binarySearch(lst, N):
    start = 0
    end = max(lst)
    maxV = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for num in lst:
            cnt += num // mid

        if cnt >= N:
            if mid > maxV:
                maxV = mid
            start = mid + 1

        else:
            end = mid - 1

    return maxV

print(binarySearch(lst, N))