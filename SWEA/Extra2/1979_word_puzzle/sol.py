import sys
sys.stdin = open('input.txt')

# 빈칸 확인 함수
def check_blank(arr, K):

    for i in range(N):
        arr[i].append(0)

    ans = 0
    for i in arr:
        point = 0
        for j in i:
            if j == 1:
                point += 1
            else:
                if point == K:
                    ans += 1
                point = 0

    return ans



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 전치 행렬
    arr_t = list(map(list, zip(*arr)))
    ans_col = check_blank(arr_t, K)

    # 기존 행렬
    ans_row = check_blank(arr, K)

    print(f'#{tc} {ans_row+ans_col}')
