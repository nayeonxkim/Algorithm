import sys
sys.stdin = open('input.txt')

def check_sudoku(arr):
    ans = 1
    # 기존 행렬
    for lst in arr:
        if len(set(lst)) != 9:
            ans = 0
            return ans

    # 전치행렬
    arr_t = list(zip(*arr))
    for lst in arr_t:
        if len(set(lst)) != 9:
            ans = 0
            return ans

    # 그룹별
    group_arr = []
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            group_arr.append(arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3])
    for lst in group_arr:
        if len(set(lst)) != 9:
            ans = 0
            return ans


    return ans

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = check_sudoku(arr)
    print(f'#{tc} {ans}')




