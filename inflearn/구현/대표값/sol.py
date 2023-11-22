import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int, input().split()))

# 1. 평균구하기
avg = round(sum(scores)/N)

# 2. 최소 차이 업데이트
min_dif = avg
min_idx = -1
min_score = avg

for i in range(N):
    # 1) 평균과의 차이
    dif = abs(avg - scores[i])

    # 2) 차이가 최소값보다 작으면 업데이트
    if dif < min_dif:
        min_dif = dif
        min_idx = i
        min_score = scores[i]

    # 3) 차이가 최소값과 같으면 조건 검사하여 업데이트
    elif dif == min_dif:
        # - 현재 점수가 최소값의 점수보다 크거나
        # - 현재 인덱스가 최소값의 인덱스보다 작으면 (차례대로 검사하기때문에 이런 일은 없음)
        if scores[i] > min_score:
            min_idx = i
            min_score = scores[i]

print(f'{avg} {min_idx+1}')