from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
arr = deque(arr)
nums = deque()
ans = ''
while arr:
    if len(arr) == 1:
        ans = 'L'
        break
    if nums:
        # 왼/오 둘 다 수열 조건만족 -> 둘 중 작은 수
        if nums[-1] < arr[0] and nums[-1] < arr[-1]:
            if arr[0] < arr[-1]:
                nums.append(arr.popleft())
                ans += 'L'
            elif arr[0] > arr[-1]:
                nums.append(arr.pop())
                ans += 'R'
        # 왼쪽만 만족
        elif nums[-1] < arr[0]:
            nums.append(arr.popleft())
            ans += 'L'
        # 오른쪽만 만족
        elif nums[-1] < arr[-1]:
            nums.append(arr.pop())
            ans += 'R'
        # 왼/오 둘 다 수열 조건에 만족하지 않음
        else:
            break
    else:
        if arr[0] < arr[-1]:
            nums.append(arr.popleft())
            ans += 'L'
        else:
            nums.append(arr.pop())
            ans += 'R'
print(len(ans))
print(ans)