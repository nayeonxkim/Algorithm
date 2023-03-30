# 전기버스2
import sys
sys.stdin = open('input.txt')


# i = 정류장 위치 | tmp = 충전 횟수
def backtracking(i, tmp):
    global cnt
    # 정류장 위치를 벗어난다면 도착한 것. (최소값과 비교)
    # 이 문제에서는 i가 n-1을 넘어갈 수 있기 때문에 부등호로 설정
    if i >= n-1:
        cnt = min(tmp, cnt)
        return
    # 시간초과를 막기 위해 더 작은 값이 안나오면 중지
    # 중간과정에서 이미 최소값을 넘으면 더 가는게 의미 X 가지치기
    if tmp >= cnt:
        return

    # 한 번 충전해서 갈 수 있는 정류장 다 둘러보는 반복문
    else:
        for j in range(1, m[i]+1):
            # 그 경우의 수에 해당하는 곳으로 다시 옮겨서 재귀
            # i의 인덱스는 0부터 시작하므로 +1
            # 부모노드에서 tmp를 가져가서 +1하므로 한 루트에 대해서만 계산함.
            backtracking(i+j, tmp+1)


T = int(input())
for tc in range(1, T+1):
    n, *m = list(map(int, input().split()))

    # 최대 이동수 : 모든 정류장에서 충전하는 경우
    # 따라서 초기 최소횟수를 n으로 설정한다.
    cnt = n
    # 시작할 때 충전하고 시작하므로 tmp 의 값을 미리 -1 해두기
    backtracking(0, -1)

    print(f'#{tc} {cnt}')
