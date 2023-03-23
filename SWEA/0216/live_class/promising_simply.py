arr = list(range(1, 11))

# 원본 배열, 사용한 원소 수 , 총합리스트(사용할 원소 담을)
def powerset(arr, K, result):

    if sum(result) > 10:
        return

    # 재귀를 언제까지?
    if K == len(arr):
        # 모든 result반환 X, 총합이 10일때만 해당 부분집합출력
        if sum(result) == 10:
            print(result)
        return
    # K는 무조건 증가
    # K번째 요소를 쓴 경우와 쓰지 않은 경우를 모두 호출한다.
    powerset(arr, K+1, result + [arr[K]])
    powerset(arr, K+1, result)

powerset(arr, 0, [])
