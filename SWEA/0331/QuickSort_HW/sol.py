import sys
sys.stdin = open('input.txt')

def hoare(arr, l, r):

    pivot = arr[l]

    i = l
    j = r

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(arr, l, r):

    if l < r:
        s = hoare(arr, l, r)
        # 피봇이었던 값은 빼고, 양 옆만 데이터로 잡음
        qsort(arr, l, s-1)
        qsort(arr, s+1, r)


for _ in range(3):
    arr = list(map(int, input().split()))

    qsort(arr, 0, len(arr)-1)
    print(*arr)