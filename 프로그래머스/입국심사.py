def isPossible(mid, n, times):
    cnt = 0

    for time in times:
        cnt += mid // time

        if cnt >= n:
            return True
    return False

def solution(n, times):
    answer = n * max(times)

    start = 1
    end = n * max(times)

    while start <= end:
        mid = (start + end) // 2

        if isPossible(mid, n, times):
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1

    return answer

