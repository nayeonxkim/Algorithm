import sys
sys.stdin = open('input.txt')

N = int(input())

for t in range(1, N+1):
    word = input()
    word = list(word.lower())
    if word == list(reversed(word)):
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')