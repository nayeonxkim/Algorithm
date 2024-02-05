import sys
sys.stdin = open('input.txt')

# 재귀함수
res = ''
def toBinary(N):
    # 종료조건
    if N == 0:
        return
    
    # 답 업데이트
    global res
    res += str(N%2)
    
    # 재귀호출
    toBinary(N//2)


# 뒤집어서 답 출력
N = int(input())
toBinary(N)
ans = list(reversed(res))
print("".join(ans))
