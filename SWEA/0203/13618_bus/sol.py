'''

버스 노선 2개
노선 1번: 1~3 정류장
노선 2번: 2~5 정류장
5개 버스 정류장
1 : 1
2 : 2
3 : 2
4 : 1
5 : 1
1 2 2 1 1

cnt = [0] * 5001
# 노선 N개 대하여 반복
    # 노선 시작과 끝 입력받음 = 1, 3
    # cnt에 추가 = [0, 1, 1, 1, 0, 0, ... ]

# 완성된 cnt = [0, 1, 2, 2, 1, 1, 0, 0, ...]

각 정류장의 노선 개수 리스트 stop_N = [0] * M
# 정류장 M개 대하여 반복
    # stop_number 입력받아
    # stop_N[stop_number] = cnt[stop_number]

# stop_N 리스트 출력

'''


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001
    for n in range(N):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            cnt[i] += 1

    M = int(input())
    stop_N = [0] * M
    for m in range(M):
        stop_number = int(input())
        stop_N[stop_number-1] = cnt[stop_number]

    print(f'#{tc}',*stop_N)
