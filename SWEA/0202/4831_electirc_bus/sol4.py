'''


충전소 위치가, 이전 위치보다는 크고

현재 위치보다는 작거나 같다.


'''


import sys
sys.stdin = open('input.txt')

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

