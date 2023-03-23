'''

A = 1 ~ 12
N개 원소의 합이 K인 부분집합의 개수 출력

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1, 13))

for tc in range(1,T+1):
    N, K = map(int, input().split())

    res = 0
    # 1을 12번 밀면서 이진수로 000000000000~111111111111 생성
    for i in range(1, 1<<12):
        subset = []
        for j in range(12):
            # 이진수와 비교하여 각 자리에 1 = 그 자리와 일치하는 곳의 리스트 값이 있는 부분집합
            # 예) 000000000011 = {11, 12}
            # 모든 부분집합을 리스트로 생성
            # [1] ~ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            if i & (1<<j):
                subset.append(A[j])

        # 리스트의 길이가 N이고, 리스트 요소의 합이 K면 res에 1추가
        if (len(subset) == N) and (sum(subset) == K):
            res += 1

    # 결과 출력 : if에 해당하는 부분집합이 없으면 res의 기본값인 0 반환
    print(f'#{tc} {res}')
