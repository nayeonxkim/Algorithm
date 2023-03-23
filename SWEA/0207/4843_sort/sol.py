'''

입력
10
1 2 3 4 5 6 7 8 9 10

출력
10 1 9 2 8 3 7 4 6 5
---

가장 큰수, 가장 작은수, 2번째 큰수, 2번째 작은수
-> 짝수 인덱스는  오름차순
-> 홀수 인덱스는 내림차순
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N - 1):
        if i % 2:
            minIdx = i
            for j in range(i+1, N):
                if numbers[minIdx] > numbers[j]:
                    minIdx = j
            numbers[minIdx], numbers[i] = numbers[i], numbers[minIdx]
        else:
            maxIdx = i
            for j in range(i+1, N):
                if numbers[maxIdx] < numbers[j]:
                    maxIdx = j
            numbers[maxIdx], numbers[i] = numbers[i], numbers[maxIdx]

    ans = numbers[:10]
    print(f'#{tc}', *ans)