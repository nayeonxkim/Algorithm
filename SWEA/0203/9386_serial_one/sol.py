'''

연속한 1의 개수중 최대값

0011001110
-> 1이 나오면 point += 1
-> point_list (0*N개) 에 point 추가
[0, 0, 1, 2, 0, 0, 1, 2, 3, 0]
-> 0이 나오면 point = 0

point_list의 최대값 출력

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = str(input())

    # 연속한 1의 개수 : point_list 생성
    point = 0
    point_list = [0] * N
    for i in range(N):
        if numbers[i] == '0':
            point = 0
        else:
            point += 1
        point_list[i] = point

    # 1의 개수 중 최대 값 : point_list의 최대값
    maxP = 0
    for p in point_list:
        if maxP < p:
            maxP = p

    print(f'#{tc} {maxP}')