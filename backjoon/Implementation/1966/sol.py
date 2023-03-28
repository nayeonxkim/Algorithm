import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(enumerate(map(int, input().split())))

    # 0번부터 가장 큰 수 고정.
    for n in range(N-1):
        # start = 가장 큰 수를 고정할 위치
        start = n

        # N번 반복
        # pop, append하면 숫자들의 위치가 바뀌는데
        # 밑에있는 for문 하나만 쓰면 "위치"만 기준으로 하기때문에
        # 수들을 건너뛸 수도 있다.
        # 따라서 계속 처음부터 끝까지 검사하도록 하기위해 for문을 하나 더 써줬다.
        for _ in range(N):
            # start 다음 숫자부터 끝까지
            # start보다 큰지 비교한다.
            # 만약 start보다 큰 수가 있다면, start를 pop하고 가장 마지막에 append한다.
            for i in range(start+1, N-start):
                if lst[start][1] < lst[i][1]:
                    lst.append(lst.pop(start))
                    break
                    # 이미 자리를 바꿨다면 for문 종료

    # 해당 인덱스 숫자가 lst의 몇번째에 있는지 출력
    for i in range(N):
        if lst[i][0] == M:
            ans = lst.index(lst[i])
    print(ans+1)