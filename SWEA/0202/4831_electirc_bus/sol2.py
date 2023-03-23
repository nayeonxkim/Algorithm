import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stop_charge = list(map(int, input().split()))

    # 무조건 최대로 이동
    # 이동해서 충전되면 충전 후 이동
    # 이동해서 충전 안되면 뒤로 이동해서 확인
    # 도착 지점이상으로 가면 이동 횟수 출력

    # 만약, 시작점이나 이미 충전한 곳으로 돌아오면 0반환
    bus_location = K
    count = stop_0 = stop_used = 0

    while True:
        if bus_location in stop_charge:
            stop_used = bus_location
            bus_location += K
            count += 1

        else:
            bus_location -= 1

        if bus_location == stop_0 or bus_location == stop_used:
            ans = 0
            break

        if bus_location >= N:
            ans = count
            break

    print(f'#{tc} {ans}')