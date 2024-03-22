import sys
sys.stdin = open('input.txt')
from collections import deque

num, N = map(int, input().split())

stack = deque()
