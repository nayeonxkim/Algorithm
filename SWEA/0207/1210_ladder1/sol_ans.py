# 1210 사다리
# 100 x 100 크기의 2차원 배열로 주어진 사다리
# 도착 인덱스에서 위로가는 방식 했음
import sys
sys.stdin = open('input.txt')
T = 10

for tc in range(T):
    testcase = int(input())  # tc
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r, c = 0, 0  # 방향제어

    for i in range(100):  # 도착점 인덱스 먼저 찾음
        if ladder[99][i] == 2:
            c = 99
            r = i  # 종료 지점 row index
            break

    while c != 0:
        if r - 1 >= 0 and ladder[c][r - 1] == 1:  # 왼쪽으로 갈 수 있을 떄
            while r - 1 >= 0 and ladder[c][r - 1] == 1:
                r -= 1

        elif r + 1 < 100 and ladder[c][r + 1] == 1:  # 오른쪽으로 갈 수 있을 때
            while r + 1 < 100 and ladder[c][r + 1] == 1:
                r += 1

        c -= 1  # 양옆 막히면 다시 위로 감

    print(f'#{testcase}', r)