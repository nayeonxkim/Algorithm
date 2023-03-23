import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    # 모든 행의 첫 열은 1
    for i in range(N):
        arr[i][0] = 1
    # 1 0 0
    # 1 0 0
    # 1 0 0

    # 첫 번째 행과 열은 계산할 필요없음
    # 두 번째 행, 열부터 계산 : (1, N)
    # 왼쪽 위 + 오른쪽 위 값
    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    # 1 0 0
    # 1 1 0
    # 1 2 1


    print(f'#{tc}')
    # 출력조건 1: 행별로 한 줄씩 출력 -> for문
    # 출력조건 2: 오른쪽에 남은 0빼고 출력 -> i열까지만 슬라이싱 [:i+1]
    # 출력조건 3: 숫자만 띄어쓰기로 구분하여 출력 -> 언패킹 *
    for i in range(N):
        print(*arr[i][:i+1])
