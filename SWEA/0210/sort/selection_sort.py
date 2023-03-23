'''
8
6 2 25 1 72 7 43 6


선택 정렬
제일 작은 값을 제일 왼쪽에 고정시켜둔다.
요소를 순회하면서 해당 요소와 전체값을 비교하여 최소값을 업데이트한다.
업데이트한 최소값을 가장 왼쪽에 고정시킨다. -> '가장 왼쪽'이 한 칸씩 밀리는 형태

'''

arr = [5, 3, 8, 1, 2, 7]

for i in range(len(arr)):
	minIdx = i
	for j in range(i+1, len(arr)):
		if arr[minIdx] > arr[j]:
			minIdx = j
	arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)