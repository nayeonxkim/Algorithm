import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    # pop, append하면 위치가 바뀌니까 인덱스 리스트를 만듦.
    idx_lst = list(range(M))


    while True:

        # 화덕의 크기만큼 /7 3 6/ 5 3
        # 2로 나눈다.
        for i in range(N):
            pizza[i] //= 2

        # 2로 나누는게 끝나면, 앞에 세 개중에 0인 값을
        # 제일 뒤로 보내고 인덱스도 뒤로 보낸다.
        # 1 0 1 5 3 -> 1 1 5 3 0
        # 0 1 2 3 4 -> 0 2 3 4 1
        for j in range(N):
            if pizza[j] == 0:
                pizza.append(pizza.pop(j))
                idx_lst.append(idx_lst.pop(j))

        # 1개 빼고 0인 경우에는 멈춘다.
        if pizza.count(0) == M-1:
            break

    print(f'#{tc} {idx_lst[1]}')
