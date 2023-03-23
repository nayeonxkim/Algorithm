import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())

    # 문서를 압축해제하여 하나의 문자열로 만든다.
    file = ''
    for n in range(N):
        alpha, cnt = input().split()
        cnt = int(cnt)
        file += alpha * cnt

    # 문자열을 10개씩 끊어 출력한다.
    for n in range(len(file) // 10):
        print(file[0:10])
        file = file[10:]
    print(file)




