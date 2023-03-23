import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    while True:
        count += 1
        arr.append((arr.pop(0)) - count)

        if count == 5:
            count = 0

        if arr[-1] <= 0:
            arr[-1] = 0
            break
    print(f'#{tc+1}',*arr)