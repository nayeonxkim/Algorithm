import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(10)]

sum = [0] * 10
sum[0] = arr[0]

for i in range(1, 10):
    sum[i] = sum[i-1] + arr[i]

minD = 100
for n in sum:
    D = abs(100 - n)
    if minD >= D:
        minD = D
        ans = n
print(ans)
