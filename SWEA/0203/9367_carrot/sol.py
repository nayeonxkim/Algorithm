'''
C 리스트로 받아
[1, 2, 3, 4, 5]
[4, 5, 1, 2, 3]
[5, 4, 3, 2, 1]

# point_list 리스트에서 최대값 출력
[1, 2, 3, 4, 5] -> 5
[1, 2, 1, 2, 3] -> 3
[1, 1, 1, 1, 1] -> 1
---
# point_list 리스트 만들기
point = 1
i가 i-1보다 1많다면 point += 1
    point_list (0*N) i번 에 넣기
아니라면 point = 1
-> i-1이니까 N+1까지 반복

# point_list의 최대값 출력

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot_size = list(map(int, input().split()))

    # point_list 만들기
    point_list = [1] * N
    point = 1
    for i in range(1, N):
        if carrot_size[i] - carrot_size[i-1] == 1:
            point += 1
        else:
            point = 1
        point_list[i] = point

    # point_list에서 최대값 출력
    print(f'#{tc} {max(point_list)}')

