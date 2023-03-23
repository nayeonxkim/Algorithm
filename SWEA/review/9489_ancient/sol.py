import sys
sys.stdin = open('input.txt')

# 행 별로 1의 최대 개수 구하는 함수
def check_one(arr):

    # 행/열의 크기가 다르므로 N, M대신에 직접 len으로 길이구한다.
    # N, M쓰면 전치행렬에서 error발생
    max_point = 0
    for i in range(len(arr)):
        point = 0
        for j in range(len(arr[i])):
            # 1이면 point +1
            if arr[i][j] == 1:
                point += 1
                # 기존 최대값보다 point가 커지면 갱신
                if max_point < point:
                    max_point = point
            # 0이면 point 0으로 리셋
            else:
                point = 0

    return max_point


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 기존 행렬
    ans_row = check_one(arr)

    # 전치 행렬
    arr_t = list(zip(*arr))
    ans_col = check_one(arr_t)

    # 둘 중 큰 값을 반환
    ans = max(ans_row, ans_col)
    print(f'#{tc} {ans}')