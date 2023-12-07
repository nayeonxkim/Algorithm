import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 회의가 끝나는 시간을 기준으로 오름차순 정렬
arr.sort(key=lambda x:x[1])

# 2. 가장 빨리 끝나는 회의 다음에 올 수 있는 회의 찾기 * 반복
cnt = 0
et = 0
for s, e in arr:
    if s >= et:
        et = e
        cnt += 1
print(cnt)