arr = list(map(int, input().split()))

# 1을 8번 밀 때까지 = 2의 7승까지 숫자 생성
for i in range(1, 1<<8):
	subset = []
# 이진수 1이 있는 자리 = 배열의 요소가 있는 집합
	for j in range(8):
	# 해당 위치의 배열 요소를 넣어 집합을 만든다.
		if i & (1<<j):
			subset.append(arr[j])

	if sum(subset) == 10:
		print(subset)