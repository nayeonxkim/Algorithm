'''

arr에서
lst(한 줄) 별로 확인한다.
lst에서 다시 n(한 글자)별로 확인한다.

for lst in arr:
    cnt = 0      # 줄 별로 cnt확인
    for n in lst:
        if n == 1:
            cnt += 1
        else:
        if cnt == k:
            ans += 1
            # 한 줄 안에 여러개가 나올 수 있기 때문에 0으로 초기화해준다.
            cnt = 0

'''

import sys
sys.stdin = open('input.txt')


def check_blank(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                # 단어칸이 있든 없든 리셋해주어야함.
                cnt = 0
    return ans


T = int(input())
for tc in range(1, T+1):
    N, k = map(int, input().split())
    # 0을 만나면 cnt를 리셋해주어야하기 때문에 가장 마지막 부분에 0을 padding해준다.
    # 예) 3*3배열에 0으로 패딩
    # 1 1 1 0
    # 1 0 1 0
    # 0 0 1 0
    # 0 0 0 0
    arr = [ list(map(int, input().split())) +[0] for _ in range(N)]

    ans1 = check_blank(arr)

    for i in range(N):
        for j in range(N):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ans2 = check_blank(arr)

    print(arr)

    print(f'#{tc} {ans1}')