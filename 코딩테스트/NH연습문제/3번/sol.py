import sys
sys.stdin = open('input.txt')
'''
1. 아래에서부터 한칸씩 검사

2. 1이라면
r = 변경된 행 -> r을 1씩 증가하면서 2가 있는지 & 비어있는지 확인하고 갈 행을 확정함.
i = 처음 출발한 행 

<while 문 : "다음 행이 갈 수 있는 행인지 검사하는 반복문" r이 N-1 보다 작고 r+1이 0인 경우>
3. 4방향 탐색
(1) 2가 있는 경우
바로 다음 칸으로 넘어가서 2번부터
(2) 2가 없는 경우
- 한 칸 아래가 0이라면 r+1
- 한 칸 아래에 1이 있다면 r은 거기서 멈춤

4. 가야하는 행 확정
- 원래 위치인 i행 j열 값은 0으로
- 마지막 정착지인 r행 j열은 1로
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N-2, -1, -1):
    for j in range(N):
        if arr[i][j] == 1:
            r = i

            while r < N-1 and arr[r+1][j] == 0:
                sticky = False
                for k in range(4):
                    ni, nj = r + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 2:
                        sticky = True
                        break

                if sticky:
                    break
                else:
                    if not arr[r+1][j]:
                        r += 1
            arr[i][j] = 0
            arr[r][j] = 1


for lst in range(N):
    print(arr[lst])