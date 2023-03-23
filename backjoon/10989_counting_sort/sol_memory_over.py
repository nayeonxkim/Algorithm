import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = [0] * N
for i in range(N):
    numbers[i] = int(input())

# 단순 카운트 배열 생성
cnt = [0] * max(numbers)
for n in numbers:
    cnt[n-1] += 1

# 누적 카운트 배열 생성
for i in range(1, max(numbers)):
    cnt[i] += cnt[i-1]

# 오름차순 정렬
temp = [0] * N
for i in range(N-1, -1, -1):
    cnt[numbers[i]-1] -= 1
    temp[cnt[numbers[i]-1]] = numbers[i]

for i in range(N):
    print(temp[i])