import sys
sys.stdin = open('input.txt')

def makenum(i, j, num):

    global res

    if len(num) == 7:
        num.sort()
        if num not in res:
            # 숫자 만들고 cnt + 1
            res.append(num)
        return

    # 오른쪽부터 시계방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            makenum(ni, nj, num + [arr[i][j]])


def perm(depth, r, nums):
    global cnt

    # depth:현재까지 조사한 대상의 수
    # r : 총 조사할 대상의 개수
    if depth == r:
        cnt += 1
    # check에 아직 r개 만큼 값이 채워지지 않은 경우
    else:
        # nums의 모든 대상을 조사
        for i in range(len(nums)):
            # nums의 i번째를 아직 사용한 적 없다면
            if not visited[i]:
                visited[i] = 1 # 사용표시하고
                perm(depth+1, r, nums) # 하나 조사했으니 depth에 +1, 전체 조사대상은 변하지않으므로 그대로 r
                visited[i] = 0 # 썼던거 다시 사용표시 없애기




T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    res = []
    cnt = 0
    makenum(0, 0, [])
    print(res)

    for nums in res:
        visited = [0] * 7
        perm(0, 7, nums)

    print(cnt)