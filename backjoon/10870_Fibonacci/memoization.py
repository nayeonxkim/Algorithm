
#
# memo = [0] * 11
# memo[0] = 0
# memo[1] = 1
#
# def fibo(n):
#     global memo # memoization을 위한 배열
#
#     if n >= 2 and memo[n] == 0:
#         memo[n] = (fibo(n-1) + fibo(n-2))
#     return memo[n]
#
# print(fibo(10))

memo = [0] * (10+1)
memo[0] = 0
memo[1] = 1

def fibo(n):
    global memo

    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo(n-1) + fibo(n-2))
    return memo[n]

print(fibo(10))
