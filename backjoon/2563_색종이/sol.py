import sys
sys.stdin = open('input.txt')
'''
길이는 10씩
3
3 4 5 6 7 8 9 10 11 12 13 

시작점 [left][99-under]
오른쪽으로 열칸
'''
N = int(input())
arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    left, under = map(int, input().split())
    for i in range(left, left+10):
        for j in range(99-under, 99-under-10, -1):
            arr[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            ans += 1

print(ans)