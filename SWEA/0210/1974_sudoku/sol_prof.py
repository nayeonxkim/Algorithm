import sys
sys.stdin = open('input.txt')

def sudoku(arr):
    # 행 확인
    for lst in arr:
        if len(set(lst)) != 9:
            return 0

    # 열 확인
    arr_t = list(zip(*arr))
    for lst in arr_t:
        if len(set(lst)) != 9:
            return 0

    # 그룹 확인

    for i in range(0, 3, 6):
        for j in range(0, 3, 6):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0

    # 위 세 for문에서 0을 반환하고 종료되지 않고 모두 길이가 9인 경우엔 마지막 return이 실행된다.
    return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)
    print(f'#{tc} {ans}')
