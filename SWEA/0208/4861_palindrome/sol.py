
'''

askqw
sdjfs
sdsep
dhshg
dfuhs

'''

import sys
sys.stdin = open('input.txt')


# 회문 확인 함수
def check_palin(n, m, array):
    # 배열의 행 순서대로 검사합니다.
    for i in range(n):
        # [j:j+m] : 확인해야하는 글자수만큼 잘라서 확인합니다.
        # n-m+1 : 배열의 범위를 벗어나지 않도록 합니다.
        for j in range(n-m+1):
            word = array[i][j:j+m]
            # 단어가 뒤집은 상태와 같다면 해당 단어를 문자열로 반환합니다.
            if word == word[::-1]:
                return ''.join(word)

# 배열 입력받아 확인
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 원본 행렬 생성 및 회문 검사
    arr = [list((input())) for _ in range(N)]
    ans1 = check_palin(N, M, arr)

    # 전치 행렬 생성 및 회문 검사
    for i in range(N):
        for j in range(N):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    ans2 = check_palin(N, M, arr)

    # 둘 중 None이 아닌값을 반환합니다.
    if ans1:
        ans = ans1
    else:
        ans = ans2

    print(f'#{tc} {ans}')

