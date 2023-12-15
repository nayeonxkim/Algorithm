import sys
sys.stdin = open('input.txt')
from collections import deque

prime = input()
dic = {}
for i in range(len(prime)):
    dic[prime[i]] = i
print(dic)


N = int(input())
for tc in range(1, N+1):
    subs = input()
    print(subs)




