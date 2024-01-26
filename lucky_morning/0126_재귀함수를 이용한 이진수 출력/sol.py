import sys
sys.stdin = open('input.txt')


res = ''
def toBinary(N):
    if N == 0:
        return

    global res
    res += str(N%2)
    toBinary(N//2)



N = int(input())
toBinary(N)
ans = list(reversed(res))
print("".join(ans))
