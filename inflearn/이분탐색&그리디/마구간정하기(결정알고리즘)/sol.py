'''
가장 가까운 두 말의 거리
최소 : 1
최대 : 최대 - 1

조건검사
mid값을 거리로 했을 때 모든 말이 배치될 수 있는지 검사
- 첫 마구간에 말 하나 놓기 : now = arr[0]
- C-1마리를 현재 말의 위치 + mid에 놓기 : for문
- 예를 들어 두 번째 말이 7번이다 -> 7보다 큰 마구간 중 가장 가까운 마구간에 놓는 다는 뜻 : arr for문
- 가장 가까운 마구간에 놓아야하므로 놓자마자 break
- C마리 중 한마리라도 마구간 구간 내를 벗어나면, C마리 모두 놓을 수 없다는 뜻이므로 False 리턴
- 총 C마리가 마구간 구간 내에 놓아지면 True 리턴
'''

import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
arr = list(int(input()) for _ in range(N))

# 1. 마구간 정렬
arr.sort()

# 2. 조건검사 함수
def isPossible(mid, arr, C):
    now = arr[0]
    for _ in range(C-1):
       now += mid
       for horse in arr:
           if horse >= now:
               now = horse
               break
       if now > max(arr):
           return False
    return True

# 3. 이분탐색
answer = 0
start = 1
end = max(arr) - 1

while start <= end:
    mid = (start + end) // 2

    if isPossible(mid, arr, C):
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)


