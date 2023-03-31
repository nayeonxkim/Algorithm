def partition(arr, l, r):
    # 제일 왼쪽 값을 피봇으로 한다.
    pivot = arr[l]
    # 피봇보다 큰 값을 찾으며 오른쪽으로 이동
    i = l
    # 피봇보다 작은 값을 찾으며 왼쪽으로 이동
    j = r

    while i <= j:
        # i는 피봇보다 큰 값을 찾아야함.
        # 피봇보다 작거나 같은 값이라면 뒷 칸으로 이동한다.
        while i <= j and arr[i] <= pivot:
            i += 1
        # j는 피봇보다 작은 값을 찾아야함.
        # 피봇보다 크거나 같은 값이라면 앞 칸으로 이동한다.
        while i <= j and arr[j] >= pivot:
            j -= 1
        # 교차되지 않은 상태로 while문이 종료되었다면,
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 교차되었다면,피봇과 작은 값의 자리를 바꾼다.
    # pivot이라고 쓰면 안되는 이유 : 그럼 피봇 자리의 값은 안바뀜.
    arr[l], arr[j] = arr[j], arr[l]
    # 피봇의 바뀐 자리를 반환 =  데이터를 나눌 기준점
    return j


def QuickSort(arr, l, r):
    # 구간이 정상적이라면
    if l < r:
        # 파티션 작업 (왼쪽구간, 오른쪽 구간 나누기)
        s = partition(arr, l, r)
        # 왼쪽에 대해 퀵 정렬
        QuickSort(arr, l, s-1)
        # 오른쪽에 대해 퀵 정렬
        QuickSort(arr, s+1, r)


arr = [5, 4, 3, 2, 1]
QuickSort(arr, 0, 4)
print(arr)