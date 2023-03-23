'''
일반 1
모든 정류장

급행 2
A가 짝수 -> 모든 짝수
A가 홀수 -> 모든 홀수
=> 정차하는 모든 정류장

광역 3
A가 짝수 -> 4의 배수
A가 홀수 -> 3의 배수 & not 10의 배수
=> 정차하는 모든 정류장

bus_stop = [0] * 1000
등장하면 해당 인덱스에 1추가 -> 1000번하는거 좀 에반듯

lst = {
1 [2,3,4]

2 [1,3,5]

3 [4,8]
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0] * 1000
    for n in range(N):
        bus_type, A, B = map(int, input().split())

        if bus_type == 1:
            for n in range(A+1, B):
                bus_stop[n] += 1

        elif bus_type == 2:
            if A % 2:
                for n in range(A+1, B):
                    if n % 2:
                        bus_stop[n] += 1
            else:
                for n in range(A+1, B):
                    if not (n % 2):
                        bus_stop[n] += 1
        else:
            if A % 2:
                for n in range(A+1, B):
                    if (not (n % 3)) and (n % 10):
                        bus_stop[n] += 1
            else:
                for n in range(A+1, B):
                    if (not (n % 4)):
                        bus_stop[n] += 1

    print(f'#{tc} {max(bus_stop)}')
