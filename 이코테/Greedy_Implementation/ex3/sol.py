'''
3 -> 3명인 그룹


'''
import sys
sys.stdin = open('input.txt')

N = int(input())
adven = sorted(list(map(int, input().split())), reverse=True)
print(N, adven)

