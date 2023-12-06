import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

'''
<mid 찾기>
덩어리 개수 == M
-> 최소값 업데이트, end = mid - 1

덩어리 개수 < M
-> mid가 더 작아야함 (덩어리 개수가 많아지려면 한 덩어리에 더 적은 수가 들어가야해)
end = mid - 1

덩어리 개수 > M
-> mid가 더 커야함 (덩어리 개수가 적어지려면 한 덩어리에 더 많은 수가 들어가야해)
start = mid + 1
'''

'''
<적절한 mid를 찾는 조건>
리스트의 개수만큼 반복

- 첫번째 요소부터 더함 : sum_num += lst[n-1], n += 1
- 누적합이 mid를 넘어가면 덩어리 추가: cnt + 1 
- 해당 요소부터 다시 누적합 구함 : n -= 1, sum_num = 0
'''

def binarySearch(lst, M):
    start = 0
    end = sum(lst)
    minMid = end

    while start <= end:
        mid = (start + end) // 2
        
        # 1. mid 검사 조건문
        sum_num = 0
        cnt = 0
        n = 1
        while n <= N:
            sum_num += lst[n-1]
            n += 1
            if sum_num > mid:
                sum_num = 0
                cnt += 1
                n -= 1
        if sum_num:
            cnt += 1
        
        # 2. 덩어리 개수에 따라 mid 및 minMid 업데이트
        if cnt == M:
            if mid < minMid:
                minMid = mid
            end = mid - 1
        elif cnt < M:
            end = mid - 1
        else:
            start = mid + 1
    return minMid

print(binarySearch(lst, M))


