A = [10, 4, 23, 11, 65, 2, 87]

def selectionSort(a, N):
    # 가장 작은 값을 찾을 구간의 시작지점 설정 : 마지막 두 개 남을 때까지
    for i in range(N-1):
        # < 여기는 기존에 하던 것처럼 최솟값 업데이트하는 과정 >
        # 일단 시작지점에 있는 값을 최소값이라고 가정한다.
        minIdx = i
        # 제일 처음 값 다음 값부터 끝까지 새로운 구간 만듦
        # 이 구간을 순회하며 하나씩 제일 첫 값보다 작은지 비교
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        # for문을 돌면서 가장 작은 minIdx를 찾았다면, 이제 그 값을 가장 처음에 갖다놓자.
        a[i], a[minIdx] = a[minIdx], a[i]

    return A

print(selectionSort(A, len(A)))