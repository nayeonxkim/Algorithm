import sys
sys.stdin = open('input.txt')

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

# 1. 카드 정렬
cards.sort()

# 2. 이분탐색 함수
def binary_search(num, cards):

    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if cards[mid] < num:
            start = mid + 1
        elif cards[mid] > num:
            end = mid - 1
        else:
            return True

    return False

# 3. 숫자 하나씩 확인
for num in nums:

    if binary_search(num, cards):
        print(1, end=' ')
    else:
        print(0, end=' ')