'''
8
6 2 25 1 72 7 43 6

버블 정렬
오른쪽 끝에 제일 큰 수 고정
뒤에 애랑 비교해서 앞에 애가 더 크면 자리 바꿔
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

for n in range(N-1, -1, -1):
    for i in range(n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] =  arr[i+1], arr[i]
print(arr)