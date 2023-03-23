import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    N, M = len(str1), len(str2)
    exist = 0


    # str2를 순회하며 str1 덩어리가 있는지 확인합니다.
    # [i:i+N] : str1의 길이 N만큼 묶어서 확인합니다.
    # range(M-N+1) : N만큼 묶어서 확인하기 때문에 out of range되지 않도록 순회길이를 설정합니다.
    for i in range(M-N+1):
        if str1 == str2[i:i+N]:
            # str1이 존재하면 1로 업데이트
            exist = 1

    print(f'#{tc} {exist}')