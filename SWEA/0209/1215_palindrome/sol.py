import sys
sys.stdin = open('input.txt')

# 회문 확인 함수 정의
def check_palin(array, lenOfpalindrome):
    cnt = 0
    # 모든 행에 대해
    for i in range(8):
        # 정해진 회문 글자수만큼 잘라서 단어를 만든다.
        for j in range(9 - lenOfpalindrome):
            word = array[i][j:j+lenOfpalindrome]
            # 그 단어가 회문이면 1을 추가한다.
            if word == word[::-1]:
                cnt += 1
    return cnt


for tc in range(1, 11):
    length = int(input())
    arr = [list(input()) for _ in range(8)]

    # 원본 행렬에서 확인
    ans1 = check_palin(arr, length)

    # 전치 행렬에서 확인
    for i in range(8):
        for j in range(8):
            # 1 4 7
            # 2 5 8
            # 3 6 9
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ans2 = check_palin(arr, length)

    print(f'#{tc} {ans1+ans2}')