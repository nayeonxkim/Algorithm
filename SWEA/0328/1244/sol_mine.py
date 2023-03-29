import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    temp, N = input().split()

    N = int(N)
    num = list(map(int, temp))

    for _ in range(N):
        maxV = 0
        # 1부터 2까지를 기준으로 삼는다. 1일 때,
        for i in range(len(num)-1):
            # 2부터 3까지
            for j in range(i+1, len(num)):
                # 둘의 자리를 바꾼다. -> 213
                num[i], num[j] = num[j], num[i]

                # maxV 업데이트
                res = ''
                for l in range(len(num)):
                    res += str(num[l])
                if int(maxV) < int(res):
                    maxV = int(res)

                # 원 위치
                num[i], num[j] = num[j], num[i]

        num = list(map(int, str(maxV)))

    print(f'#{tc} {maxV}')
