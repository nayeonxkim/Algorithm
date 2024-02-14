import sys
sys.stdin = open('input.txt')

# 1. 입력받기
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 2. 끝나는 시간 기준으로 정렬하기
lst.sort(key=lambda x:x[1])
print(lst)

# 3. 다음 할 회의 찾기
# - 시작 시간이 이전 끝나는 시간보다 크거나 같은 것
e = lst[0][1]
cnt = 1
for i in range(1, n):
    if lst[i][0] >= e:
        cnt += 1
        e = lst[i][1]
print(cnt)