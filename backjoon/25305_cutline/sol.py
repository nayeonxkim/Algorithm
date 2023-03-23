import sys
sys.stdin = open('input.txt')

N, k = map(int, input().split())
scores = list(map(int, input().split()))

# 선택 정렬
for i in range(N-1):
    maxIdx = i
    for j in range(i+1, N):
        if scores[maxIdx] < scores[j]:
            maxIdx = j
    scores[i], scores[maxIdx] = scores[maxIdx], scores[i]

print(scores[k-1])
