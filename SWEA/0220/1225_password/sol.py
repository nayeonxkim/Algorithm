import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    que = list(map(int, input().split()))

    # 1~5 순회하면서
    # 모든 값이 0보다 클 때만 0번 값 pop해서 n만큼 빼주고
    # 계산한 값을 다시 append한다.
    Flag = True
    while Flag:
        for n in range(1, 6):
            if all(0 < x for x in que):
                que.append(que.pop(0)-n)
            else:
                Flag = False

    for i in range(8):
        if que[i] <= 0:
            que[i] = 0

    print(f'#{tc}', *que)






