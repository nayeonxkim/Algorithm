'''

1. 1000칼로리 이하 모든 조합
-> perm


2. 걔네 중에 뭐였지 맛점수 젤 높은애의 점수
#일단 따로받아보기

'''

def perm()





import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)


