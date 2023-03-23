import sys
sys.stdin = open('input.txt')

T = int(input())  # test case

for t in range(1, T+1):
    K, N, M = map(int, input().split())  # K 최대이동정류장수 N 종점 M 충전기 설치버정
    charger = list(map(int, input().split()))  # 충전기 있는 버정번호

    now = 0 # 현재 위치
    cnt = 0 # 충전횟수

    # 도착 전까지 반복
    while now + K < N:
        # 이동해서 충전소가 있으면 그 정류장으로 이동해서 충전.
        # 충전기 없으면
        for num in range(K, 0, -1):
            if (now + num) in charger: # 현재 위치+ 이동거리 이동시 충전기 있으면
                now += num # 현재위치 바꿔주고 충전횟수 더함
                cnt += 1
                break
        else: #충전기 없어서 종점까지 못가면 0 반환하고 반복문 탈출
            cnt = 0
            break

    print(f'#{t} {cnt}')