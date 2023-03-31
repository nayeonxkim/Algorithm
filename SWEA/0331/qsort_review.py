arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
N = 10

def hoare(arr, l, r):

    pivot = arr[l]

    # 양쪽 각각 조사 첫 시작점
    # 왼쪽시작점에서 오른쪽으로 이동, 오른쪽시작점에서 왼쪽으로 이동
    i = l
    j = r

    while i <= j:

        # 왼쪽에서 시작 : i
        # 정상범위 내에서 pivot보다 큰 값을 찾을 때까지 오른쪽으로 이동
        while i <= j and arr[i] <= pivot:
            i += 1

        # 오른쪽에서 시작 : j
        # 정상범위 내에서 pivot보다 작은 값을 찾을 때까지 왼쪽으로 이동
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 정상범위 안에서 i와 j의 이동이 멈추었다면, 두 값의 자리를 바꾼다.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 정상범위를 벗어나서 while문을 벗어난다면, 피봇값과 작은값(j)의 자리를 바꾼다.
    # 유의) 이때, pivot이 아니라 arr[l]을 사용해야한다.
    # -> pivot을 사용하면 피봇 자리의 값은 arr[j]로 바뀌지 않는다.
    arr[l], arr[j] = arr[j], arr[l]

    # 바뀐 pivot의 위치를 반환하여, 데이터 분할 시의 기준점으로 삼는다.
    return j


def qsort(arr, l, r):

    if l < r:
        # 데이터 분할 기준점
        partition = hoare(arr, l, r)
        # 왼쪽 구간에서 퀵 정렬 과정 수행
        qsort(arr, l, partition-1)
        # 오른쪽 구간에서 퀵 정렬 과정 수행
        qsort(arr, partition+1, r)

qsort(arr, 0, N-1)
print(arr)