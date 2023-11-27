import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))

    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] < A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    print(A[2])