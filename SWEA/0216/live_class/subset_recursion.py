def f(i, k, key):
    # 모든 원소에 대해 모든 경우의 수를 확인했다면, 함수를 종료한다.
    # 부분집합 완성
    if i == k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]

        if s == key:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()

    # 아직 확인할 원소가 남았다면
    else:
        bit[i] = 1
        f(i+1, k, key)
        bit[i] = 0
        f(i+1, k, key)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
key = 10
bit = [0] * N
f(0, N, key)