import sys
sys.stdin = open('input.txt')

# 재귀함수
res = ''
def toBinary(N):
    if N == 0:
        return

    global res
    res += str(N%2)
    toBinary(N//2)

# 뒤집어서 답 출력
N = int(input())
toBinary(N)
ans = list(reversed(res))
print("".join(ans))
