import sys
sys.stdin = open('input.txt')

def digit_sum(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans


N = int(input())
nums = list(map(int, input().split()))

max = 0

for n in nums:
    sum = digit_sum(n)
    if sum > max:
        max = sum
        max_num = n
print(max_num)