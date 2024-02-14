import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))


def sol(array, n):

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if array[j] < array[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    return max(dp)

print(sol(lst, N))

