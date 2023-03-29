import sys
sys.stdin = open('input.txt')

# 숫자 리스트, 교환횟수
def change(numbers, cnt):
    # result = [[], []]
    global result

    temp = ''

    # [1, 2, 3] 순회하면서 temp에 추가
    for number in numbers:
        # temp == 123
        temp += number

    # result[1] : result의 제일 마지막 자리에 123이 있다면 반환 후 종료
    if int(temp) in result[cnt]:
        return
    # result[1] : 없다면 추가
    # result[1] = 123
    else:
        result[cnt].append(int(temp))

    if cnt == 0:
        return

    # n = 3
    n = len(numbers)

    # 0부터 2까지 순회
    for i in range(n):
        # 1부터 2까지 순회
        for j in range(i + 1, n):
            # 바로 뒷 숫자랑 자리 바꿈
            numbers[i], numbers[j] = numbers[j], numbers[i]

            # cnt자리를 왼쪽으로 한칸 옮겨서 다시 호출
            change(numbers, cnt - 1)

            # 다시 자리 바꿈
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for t in range(1, T + 1):
    # 123, 1
    temp, cnt = input().split()

    # numbers = ['1', '2', '3']
    numbers = list(temp)

    # [[], []]
    result = [[] for _ in range(int(cnt) + 1)]

    change(numbers, int(cnt))
    print(result)
    print('#{} {}'.format(t, max(result[0])))