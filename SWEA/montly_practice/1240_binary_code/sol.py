import sys
sys.stdin = open('input.txt')

num = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1],
       [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1],
       [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]


def check_code(code):
    odd = even = 0

    if code:
        # 유효성 검사
        for i in range(8):
            if i % 2:  # 짝수인덱스 = 홀수번째면
                even += code[i]
            else:
                odd += code[i]
    else:
        return 0

    if (odd * 3 + even) % 10:
        return 0
    else:
        return sum(code)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    for lst in arr:
        if all(i == 0 for i in lst):
            arr.remove(lst)

    lst = arr[0]

    code = []
    for i in range(M-6):
        for n in range(10):
            if lst[i:i+7] == num[n]:
                for j in range(7):
                    lst[i+j] = -1
                code.append(n)

    ans = check_code(code)
    print(f'#{tc} {ans}')