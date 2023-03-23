'''


10 * 10
color_zone1 = [2,2]부터 [4,4]까지 color1
color_zone2 = [3,3]부터 [6,6]까지 color2
color1과 color2가 겹치는 구간 ?


'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 색칠할 10 * 10 격자 생성
    zone = [[0] * 10 for i in range(10)]

    # 색칠 zone 정보 입력받는다.
    for n in range(N):
        start_row, start_col, end_row, end_col, color = map(int, input().split())

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        # 색칠 시작지점부터 끝지점까지 한 칸씩 이동하며 color 값을 더해준다.
        for row in range(start_row, end_row+1):
            for col in range(start_col, end_col+1):
                zone[row][col] += color
        print(zone)

    # 빨강(1) + 파랑(2)이 모두 칠해진 보라색(3) 칸의 개수를 세어 반환한다.
    res = 0
    for row in range(10):
        for col in range(10):
            if zone[row][col] == 3:
                res += 1

    print(f'#{tc} {res}')
