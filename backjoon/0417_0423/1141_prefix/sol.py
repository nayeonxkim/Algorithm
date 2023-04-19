
import sys
sys.stdin = open('input.txt')

N = int(input())
words = [input() for _ in range(N)]

# 길이 오름차순
for i in range(N-1):
    for j in range(i+1, N):
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]

res = words[:]
for i in range(N):
    for j in range(i+1, N):
        if words[j][:len(words[i])] == words[i]:
            res.remove(words[i])
            break

print(len(res))

