A = [1, 3, 6, 13, 26, 57, 88]

def binarySearch(a, N, key):
    start = 0
    end = N - 1
    # 검색 구간이 남아있으면 계속 검색한다.
    # *검색구간이 남아있다?* 검색구간의 start지점이 end지점보다 작거나 같아야 검색이 가능하다!
    while start <= end:
        # 검색구간에서 중간위치 찾기
        middle = (start + end) // 2
        # 그 값이 내가 찾는 값과 같으면 True 반환
        if a[middle] == key:
            return True
        # 그 값이 내가 찾는 값보다 크다면 해당 값 왼쪽 부분에서 다시 검색
        elif a[middle] > key:
            # 방금 확인한 값의 왼쪽까지로 검색구간을 다시 설정한다.
            end = middle - 1
        # 그 값이 내가 찾는 값보다 작다면 해당 값 오른쪽 부분에서 다시 검색
        else:
            # 방금 확인한 값의 오른쪽부터로 검색구간을 다시 설정한다.
            start = middle + 1
    # while문을 다 돌았는데도 내가 찾는 값이 없다면 검색 실패를 반환
    return False


print(binarySearch(A, len(A), 26))
print(binarySearch(A, len(A), 52))