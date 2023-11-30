import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(9)]

def check_cnt(cnt):
    for i in range(1, 10):
        if cnt[i] != 9:
            return False
    return True

def check_sdoku(arr):
    # 1. 행 검사
    cnt = [0] * 10
    for i in range(9):
        for j in range(9):
            cnt[arr[i][j]] += 1

    if not check_cnt(cnt):
        return "NO"

    # 2. 열 검사
    cnt = [0] * 10
    for j in range(9):
        for i in range(9):
            cnt[arr[i][j]] += 1

    if not check_cnt(cnt):
        return "NO"

    # 3. 사각형 검사
    di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dj = [0, -1, 1, 0, -1, 1, 0, -1, 1]

    cnt = [0] * 10
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            for k in range(9):
                ni, nj = i + di[k], j + dj[k]
                cnt[arr[ni][nj]] += 1
    if not check_cnt(cnt):
        return "NO"

    return "YES"


print(check_sdoku(arr))