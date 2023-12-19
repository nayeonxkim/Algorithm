import sys
sys.stdin = open('input.txt')
from collections import deque
'''
생성한 check라는 빈 리스트에 CBA만 넣으면서 검사

CBDAGE
res = [C B A]

# 1. res에 현재 글자가 있다면 pass
# 2. required[p]와 현재 글자가 같다면 res에 추가, p +1
# 3. res에 있는 글자라면 함수 끝내고 NO 반환
# 4. 전부 돌고 나서 res join 값이 need와 같아면 YES 다르면 NO
'''

required = input()
N = int(input())
for tc in range(1, N+1):
    plan = input()

    res = deque()
    p = 0
    for sub in plan:
        if sub in res:
            pass
        elif sub == required[p]:
            res.append(sub)
            if p < len(required)-1:
                p += 1
        elif sub in res:
            print(f"#{tc} NO")
            break
    if ''.join(res) == required:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")



