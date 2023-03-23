'''

6 9 5 7 4
왼쪽에 나보다 높은 탑의 인덱스+1
stack = [[0, 6]]


'''

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(enumerate(map(int, input().split())))
print(arr)