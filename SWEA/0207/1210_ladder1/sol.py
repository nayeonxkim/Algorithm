import sys
sys.stdin =open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 일단 도착한 지점부터 찾는다. 도착한 지점의 row와 col로 업데이트한다.
    # 마지막 행에만 있으니 열만 바꾸면서 찾는다.
    row = 99
    for j in range(100):
            if arr[row][j] == 2:
                col = j
                # 찾으면 바로 나올 수 있게 break해주자
                break
    # 첫 출발 지점 = 2가 있는 자리.
    # 내 위치 = row, col

    # 사다리 범위를 벗어나지 않을 때까지는 계속 위로 올라감.
    while row >= 0:
        #근데 좌우에 길이 있으면 좌우 먼저 가야됨
        # 길이 있고 (1), 사다리 범위 안에 있으면 길이 끊길 때까지 계속 간다.
        # 범위 안에 있는지 먼저 확인해야함 !!!!

        # 왼쪽으로 간다. : col -1
        if col - 1 >= 0 and arr[row][col-1]:
            while col - 1 >= 0 and arr[row][col-1]:
               # 계속 왼쪽으로 간다.
               col -= 1
        # 오른쪽으로 간다. : col +1
        elif col + 1 < 100 and arr[row][col+1]:
            while col + 1 < 100 and arr[row][col+1]:
                col += 1

        # 좌우 모두 갈 수 없으면 위로 올라간다.
        row -= 1

    # 사다리 출발 지점의 열 반환
    print(f'#{tc} {col}')















