'''
왼쪽부터 차례대로 더하거나 곱해서 가장 큰 수 만들기
'''

import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input()))

res = numbers[0]
for i in range(1, len(numbers)):
    if res == 0 or numbers[i] == 0 or numbers[i] == 1:
        res += numbers[i]
    else:
        res *= numbers[i]
        
print(res)