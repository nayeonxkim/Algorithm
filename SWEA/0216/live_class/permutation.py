
def permutation(i, K, res): # 시작, 뽑는 원소의 개수, 완성된 집합들의 개수

    if i == K:
        print(res)
        return




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
        powerset(arr, K + 1, result + [arr[K]])
        powerset(arr, K + 1, result)