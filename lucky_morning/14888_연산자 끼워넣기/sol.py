from itertools import permutations
import sys
sys.stdin = open('input.txt')

# 1. 입력받기
N = int(input())
lst = list(map(int, input().split()))
p, m, mt, dv = map(int, input().split())

# 2. 순열로 연산자의 모든 경우의 수 찾음
operator = list(permutations(p * '+' + m * '-' + mt * '*' + dv * '/', N-1))

# 3. 초기 최대/최소값 설정
maxV = 0
minV = 100 * 11

# 4. 연산자 리스트 순서대로 순회.
for op in operator:
    
    # 4-1) 초기값 세팅
    i = 0
    res = lst[0]
    # 4-2) 연산자 리스트 요소를 순회하며 차례대로 계산
    while i < N-1:
        if op[i] == '+':
            res += lst[i+1]
        elif op[i] == '-':
            res -= lst[i+1]
        elif op[i] == '*':
            res *= lst[i+1]
        else:
            if res < 0:
                res = -(abs(res)//lst[i+1])
            else:
                res //= lst[i+1]
        i += 1
    # 4-3) 모든 계산이 끝난 후 최대/최소값 업데이트
    if res > maxV:
        maxV = res
    if res < minV:
        minV = res
        
# 5. 출력
print(maxV)
print(minV)