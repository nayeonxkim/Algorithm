# 당근 문제의 가로 세로 버전
# 델타 탐색하면 겹치는 애들 다 조사해버림
import sys
sys.stdin = open('input.txt')

# 각 행 별로 연속하는 1의 최대개수 구하는 함수
def cnt_one(arr):
    # mx가 for문 밖에 있는 이유
    # 모든 행을 다 조사하여 그 중에 cnt가 가장
    # 큰 값을 mx에 할당해야하므로
    # 행을 순회할때마다 초기화 되면 안된다.
    mx = 0
    for lst in arr:
        # cnt가 for문 안에 있는 이유
        # 행 별로 1의 수를 조사해야하므로
        # 행을 순회할 때마다 초기화되어야한다.
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1

                # mx값을 업데이트하면서 가장 큰 1의 연속개수만 저장한다.
                if mx < cnt:
                    mx = cnt

            else:
                cnt = 0
    return mx

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 기존 배열
    ans_row = cnt_one(arr)

    # 전치행렬
    arr_t = list(zip(*arr))
    ans_col = cnt_one(arr_t)

    ans = max(ans_row, ans_col)
    print(f'#{tc} {ans}')




