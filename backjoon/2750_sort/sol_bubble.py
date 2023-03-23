import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [0] * N
for n in range(N):
    arr[n] = int(input())

# [요소 하나가 돌아가면서 전체와 비교 -> 걔 오른쪽에 고정 ] 반복
# 오른쪽 끝에 제일 큰 수 고정
for n in range(N-1, 0, -1):
    # n을 하나씩 줄이면서 비교
    for i in range(n):
        # 앞에 수가 더 크면 뒤에 수랑 자리 바꿈
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
for i in range(N):
    print(arr[i])


