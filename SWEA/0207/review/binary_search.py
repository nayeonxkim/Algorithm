'''
9
7 2 4 11 23 9 1 8 35
8
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
key = int(input())

start = 0
end = N - 1

while start <= end:
    middle = (start + end) // 2
    if arr[middle] == key:
        print(middle)
        break
    elif arr[middle] > key:
        end = middle - 1
    else:
        start = middle + 1

    if start > end:
        print('해당 값이 없습니다.')
