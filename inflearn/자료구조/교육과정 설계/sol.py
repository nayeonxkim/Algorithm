import sys
sys.stdin = open('input.txt')
from collections import deque
'''
생성한 res라는 빈 리스트에 CBA만 넣으면서 검사

'''
prime = input()
dic = {}
for i in range(len(prime)):
    dic[prime[i]] = i
print(dic)


N = int(input())
for tc in range(1, N+1):
    subs = input()
    print(subs)




