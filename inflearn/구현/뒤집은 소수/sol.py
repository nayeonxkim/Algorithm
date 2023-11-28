import sys
sys.stdin = open('input.txt')

def reverse(x):
    ans = ''
    while x:
        ans += str(x % 10)
        x //= 10
    return int(ans)

def IsPrime(x):
    cnt = 0
    for n in range(1, x+1):
        if x % n == 0:
            cnt += 1

    if cnt == 2:
        return True


N = int(input())
nums = list(map(int, input().split()))

for n in nums:
    rv_n = reverse(n)
    if IsPrime(rv_n):
        print(rv_n, end=' ')
