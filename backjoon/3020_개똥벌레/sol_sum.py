import sys
sys.stdin = open('input.txt')

# 1. 입력받기
n, h = map(int, input().split(" "))


# 2. 각 장애물의 시작과 끝만 기록
lst = [0] * h

for i in range(n):
    stick = int(sys.stdin.readline())

    # 짝수면 0에서 시작
    if i % 2 == 0:
        lst[0] += 1
        lst[stick] -= 1

    # 홀수면 h-1-stick 에서 시작
    else:
        lst[h-stick] += 1

# 3. 누적합으로 각 층별 장애물 개수 계산
for j in range(1, h):
    lst[j] += lst[j-1]

# 4. 최소값과 그 층의 개수
minV = min(lst)
cnt = 0
for n in lst:
    if n == minV:
        cnt += 1

# 5. 정답 출력
print(minV, cnt)

