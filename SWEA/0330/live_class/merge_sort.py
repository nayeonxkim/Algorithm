def merge(left, right):
    pass


def msort(arr):            # start, end
    if len(arr) == 1:      # arr가 한 칸이 된다면 함수 끝
        return arr

    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]

    left = msort(left)
    right = msort(right)
    return merge(left, right)

N = int(input())
arr = list(map(int, input().split()))

msort(arr)