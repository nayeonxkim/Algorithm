
def f(i, N, s, key): # i원소, N집합의 크기, s i-1까지 포함된 원소의 합, key 목표값
    global cnt
    global fcnt
    fcnt += 1

    # 내가 찾는 값보다 합이 커진 경우, 더이상 더해봤자 답이 될 수 없기 때문에
    # 재귀를 멈춘다.
    if s > key:
        return

    # 이미 내가 찾는 값이 되었기 때문에 남은 원소는 고려하지 않아도 됨.
    elif s == key:
        cnt += 1
        return

    # 모든 원소 고려 마쳤음.
    elif i == k:
        return
    else:
        # A[i]가 포함되는 경우 : 기본형
        f(i+1, N, s+A[i], key)
        # A[i]를 포함시키지 않는 경우
        f(i+1, N, s, key)



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
key = 10
cnt = 0
bit = [0] * N

f(0, N, 0, key)