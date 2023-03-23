'''
8
6 2 10 1 3 7 5 6

10 이하의 자연수를 오름차순 정렬하라.

카운팅 정렬 : 배열에서 max인 숫자가 작을 때 유용
'''

arr = [7, 2, 3, 5, 7, 1, 4, 6, 7, 5, 0, 1]

cnt = [0] * (max(arr) + 1) # cnt의 인덱스 : 0 ~ 7
for i in range(len(arr)):
	cnt[arr[i]] += 1

print(cnt)

sorted_arr = []
for i in range(len(cnt)):
    for _ in range(cnt[i]):
        sorted_arr.append(i)
print(sorted_arr)