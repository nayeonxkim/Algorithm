import sys
sys.stdin = open('input.txt')

T = int(input())
# 각 테스트케이스마다 입력값 받음
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 정수 리스트에서 가장 큰 수와 가장 작은 수를 구함
    maxN = 0
    minN = numbers[0]
    for n in numbers:
        if maxN < n:
            maxN = n
        if minN > n:
            minN = n

    # 가장 큰 수와 가장 작은 수의 차이를 계산하여 출력함
    ans = maxN - minN
    print(f'#{tc} {ans}')

