def solution(arr, K, result):

    if result != 10:
        return

    for i in range(1, K+1):
        if arr[i]:
            print(data[i], end = ' ')
    print()


def make_candidates(arr, K, N, c):
    c[0] = True # 해당 원소를 사용한다.
    c[1] = False # 해당 원소를 사용하지 않는다.
    return 2

def backtracking(arr, K, N, result):
    if result > 10:
        return
    # 총합 계산은 result 변수로 진행
    # 후보군 목록 생성
    c = [0] * 2
    # 부분집합에 해당 원소를 쓸 것인지 말것인지 구분하는 용도. 1이면 쓴다.
    # 해당 원소를 쓸지말지 결정 -> 경우의 수 2개

    # 언제까지 조사?
    # 현재 조사하는 위치가 종료지점에 도달할 때까지
    if K == N:
        solution(arr, K, result)
    # 아직 조사할 원소가 남았다면
    else:
        K += 1

        ncandidates = make_candidates(arr, K, N, c)
        for i in range(ncandidates): # 후보군 수만큼
            arr[K] = c[i]
            if arr[K]: # K번째 원소를 쓰기로 했으면
                # 총합에 원본 데이터의 K번째 원소의 값을 더한다.
                backtracking(arr, K, N, result + data[K])

            else: # K번째 원소를 쓰지 않으면
                # 총합에 K번째 원소는 더하지 않고 다음 조사 대상을 조사하러 간다.
                backtracking(arr, K, N, result)


# 유망성 조사를 위한 변수
MAXCANDIDATES = 12 # 최대 후보군 수 지정
NMAX = 12 # 최대 원소수 : 적당히 큰 수

data = list(range(11))
arr = [0] * NMAX # 각 원소를 사용할 것인지 체크할 배열


# 조사 시작
# 체크할 배열, 시작점, 종료지점, 총합
backtracking(arr, 0, 10, 0)