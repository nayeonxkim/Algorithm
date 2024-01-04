import sys
sys.stdin = open('input.txt')

N = int(input())
print(N)

'''
- now의 길이가 N이 되면 끝
- now가 좋은 수열이 아니라면 끝


1부터 하나씩 붙이면서



체크 함수
- 조사 길이를 1부터 len(now)의 반까지 1씩 늘림
- 현재 조사 구간이, 그 길이만큼 뛰어넘은 다음 구간과 일치하면 False
'''
def not_good(now):
    # now가 좋은 수열이면 False
    for i in range(1, len(now)//2 +1):
        pass
    if 어쩌구:
        return False
    else:
        return True


ans = 0

def backtrack(now):
    global ans

    if not_good(now):
        return

    if len(now) == N:
        ans = min(ans, int(now))

    backtrack(now + '1')
    backtrack(now + '2')
    backtrack(now + '3')


backtrack('')
print(ans)