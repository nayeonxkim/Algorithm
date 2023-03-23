# 수의 대소만 확인할 수 있으면 됨
'''
입력값
1000 999 1000 999 1000 999

수의 대소 = 인덱스
[999 1000]

입력값 리스트를 수의 대소에 따라 값을 바꿈 : 수의 대소 리스트의 인덱스 = 입력값 리스트의 값
1 0 1 0 1 0
---
# 리스트 자체가 바뀌면 안되기 때문에 입력받은 리스트를 얕은 복사해서 사용한다.

## 인덱스 리스트 만들기 : idx_list
# 복사한 리스트 X_copy를 버블 정렬로 오름차순 정렬한다.
# 번호당 하나의 인덱스만 가져야하므로 idx_list를 생성하여, 이미 존재하지 않는 숫자만 idx_list에 넣는다.

## X의 값을 인덱스로 바꾸기
[2 4 -10 4 -9]
X[2] = idx_list.index(X[2])
# 위 과정을 2부터 -9까지 반복
# X의 모든 요소에 대해 for문
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
X = list(map(int, input().split()))
X_copy = list(set(X))

idx = [0] *



for i in range(N):
    X[i] = X_copy.index(X[i])

## X출력
print(*X)
