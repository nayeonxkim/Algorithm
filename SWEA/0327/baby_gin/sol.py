import sys
sys.stdin = open('input.txt')

# 모든 수 순열 만들기 : 재귀
def perm(i, k):
    global res

    # 제일 마지막 호출부터
    if i == k:

        # [1,2,4,7,8,3]
        # [1,2,4] [7,8,3]
        left = p[:3]
        right = p[3:]

        ans = 0
        ## 왼쪽 세 개 먼저 조사

        if left[0] + 1 == left[1] and left[1] + 1 == left[2]:
            ans += 1
        elif left[0] == left[1] and left[1] == left[2]:
            ans += 1

        if right[0] + 1 == right[1] and right[1] + 1 == right[2]:
            ans += 1
        elif right[0] == right[1] and right[1] == right[2]:
            ans += 1

        if ans == 2:
            res.append(True)
        else:
            res.append(False)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]



T = int(input())
for tc in range(1, T+1):
    p = list(map(int, input()))

    res = []
    perm(0, 6)

    if True in res:
        print(True)
    else:
        print(False)


