import sys
sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스마다 입력값 받기
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 정수 리스트를 차례대로 순회하면서 M개씩 합을 구함
    # 리스트 범위를 벗어나면 안되기 때문에 N-M개까지만 순회하며 합을 구한다.
    sum_list = [0] * (N-M+1)
    for i in range(N-M+1):
        sumN = 0
        for j in range(M):
            sumN += numbers[i+j]
            sum_list[i] = sumN

    # 가장 큰 합과 가장 작은 합을 구함
    maxS = 0
    minS = sum_list[0]
    for n in sum_list:
        if maxS < n:
            maxS = n
        if minS > n:
            minS = n

    # 가장 큰 합과 가장 작은 합의 차이를 구해 출력함
    ans = maxS - minS
    print(f'#{tc} {ans}')