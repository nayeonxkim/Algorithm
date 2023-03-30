def binarySearch(arr, start, end, key):
    if start > end:  # 검색구간이 끝났는데도 key값을 찾지 못하면 -1 반환
        return -1

    else:
        mid = (start+end)//2

        if key == arr[mid]:
            return mid

        elif key < arr[mid]:
            return binarySearch(arr, start, mid-1, key)
        else:
            return binarySearch(arr, mid+1, end, key)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binarySearch(arr, 0, len(arr)-1, 10))