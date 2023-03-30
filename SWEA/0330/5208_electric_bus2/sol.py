'''
N = 5
2 3 1 1 X

0번 정류장에서 갈 수 있는 모든 경우의 수
((이동한 정류장에서 갈 수 있는 모든 경우의 수))

- 0에서 1로 이동 -> 1~3칸 이동
- 0에서 2로 이동 -> 1칸 이동 -> 1칸 이동
---
(1) 재귀함수 인자
- 현재 위치(정류장 인덱스), 마지막 정류장 인덱스(고정)
- 현재 위치만 바뀜

(2) 재귀함수 구조
arr의 값에 따라 이동하는 경우의 수 달라짐 -> for문

이전 정류장까지의 이동횟수 +1

0번 -> 1번 -> 4번
    +1    +1

0번 -> 2번 -> 3번 -> 4번
    +1    +1     +1

-> 부모노드의 cnt에 +1씩

자식노드로 이동할 때 cnt+1
자식노드로 이동
다시 부모노드로 돌아오면서 cnt-1

(3) 종료조건
현재 위치가 마지막 정류장을 넘어가면 도착한 것. (도착못하는 경우X)
i가 N-1이상이면 함수 종료

(4) 백트래킹
위까지만 하면 시간 초과
"최소" 이동횟수를 구하는 것이기 때문에
이동과정 중간에 이미 기존의 최소 이동횟수를 넘어가면
더이상 이동할 필요 X

-> 따라서 cnt가 현재의 최소 이동횟수 이상이 되면 함수 종료
'''

import sys
sys.stdin = open('input.txt')

def f(i, N):
    global cnt
    global minV

    ### (4) 백트래킹 ###
    if cnt >= minV:
        return

    ### (3) 종료조건 ###
    if i >= N-1:
        if minV > cnt:
            minV = cnt
        return

    ### (2) 재귀함수 구조 ###
    for k in range(1, arr[i]+1):
        cnt += 1
        f(i+k, N)
        cnt -= 1


T = int(input())
for tc in range(1, T+1):

    # input 받음
    temp = list(map(int, input().split()))
    N, arr = temp[0], temp[1:]

    # cnt = 이동횟수, minV = 최대이동횟수는 모든 정류장을 지나는 경우인 N번
    cnt = 0
    minV = N

    ### (1) 재귀함수 인자 ###
    f(0, N)
    print(f'#{tc} {minV-1}')
