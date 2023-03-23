import sys
sys.stdin = open('input.txt')
N = int(input())
check_lst = list(map(int, input().split()))

M = int(input())
lst = list(map(int, input().split()))

check_lst.sort()

def binary(check_lst, n):

    start = 0
    end = len(check_lst) - 1

    while start <= end:

        middle = int((start + end)/2)

        if check_lst[middle] == n:
            return 1

        elif check_lst[middle] > n:
            end = middle - 1

        elif check_lst[middle] < n:
            start = middle + 1

    return 0


for n in lst:
    print(binary(check_lst, n))

# start = 0
# end = len(check_lst)
#
# while start <= end:
#
#     middle = int((start + end)/2)
#     print(middle)
#     if middle == 2:
#         print(1)
#         break
#
#     elif middle > 2:
#         end = middle - 1
#
#     elif middle < 2:
#         start = middle + 1
#
# else:
#     print(0)
