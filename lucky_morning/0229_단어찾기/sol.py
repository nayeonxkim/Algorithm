import sys
sys.stdin = open('input.txt')

N = int(input())
candidate = list(input() for _ in range(N))
real = list(input() for _ in range(N-1))

for word in candidate:
    if word not in real:
        print(word)