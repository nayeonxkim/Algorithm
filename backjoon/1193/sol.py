'''

1. 무한히 큰 배열 -> 배열 만드는 문제는 아님
2. 숫자를 미리 만들어두는게 아니라 받은 숫자를 토대로 바로 결과값 만들어야함
3. 규칙이 있다.

---
1개
1
---
2개
2
3
---
3개
4
5
6
---
4개
7
8
9
10
---
5개
11
12
13
14
15
---

=> 홀수는 역방향, 짝수는 정방향

sum(S)과 N의 차이 -> n개 만큼 리스트 만들자
정방향 : 1/ans부터 ans/1까지
'''


import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
print(N)

S = []
ans = 1
for n in range(1, N):
    S.append(n)
    if sum(S) >= N:
        S.pop()
        ans = n
        break

# 난 3개있는 칸
print(ans)
print()
res = []
D = N - sum(S) -1
for i in range(N-D, N-D+ans):
    res.append(i)
print(res)

# 홀수면 역방향
if ans % 2:
    pass
# 짝수면 정방향
else:
    pass