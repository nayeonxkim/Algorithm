import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [0] * (N+1)
cnt = 0

# 에라토스테네스 체
'''
[1, 2, 3, 4, 5, 6, 7, 8]
[0, 0, 0, 0, 0, 0, 0, 0]
-> 2부터 검사
- 0이면 이 인덱스는 소수 -> 소수 카운팅 +1
- 이 소수의 배수들에 카운트 +1 -> 0이 아니게 되므로 처음 for문을 건너뛴다.
'''
for i in range(2, N+1):
    if lst[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            lst[j] += 1

print(cnt)