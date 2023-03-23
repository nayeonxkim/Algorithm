import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    stick = list(input())

    cnt = 0
    ans = 0

    # i-1을 조사하는데 범위는 기존 범위 그대로 하면 문제가 없나?
    # 이렇게 해서 문제가 생기는 경우는 0번 인덱스일 때, out of range가 뜨는 것인데,
    # 이 문제에서는 첫 시작은 무조건 레이저나 막대기의 시작, 즉 (일 것이다.
    # ) 경우에만 i-1을 조사하기 때문에 0번 인덱스를 조사하면서 out of range가 뜨는 일은 발생하지 않는다!
    for i in range(len(stick)):
        if stick[i] == '(':
            cnt += 1
        else: # ) 인 경우
            if stick[i-1] == '(': # 앞이 (면 레이저 이므로 cnt -1하고 ans에 추가
                cnt -= 1
                ans += cnt
            else: # 앞도 )인 경우 : 막대 하나 끝남
                cnt -= 1
                ans += 1 # 한 덩어리만 나옴

    print(f'#{tc} {ans}')

