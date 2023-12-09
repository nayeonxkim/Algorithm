from collections import deque


def solution(stones, k):
    answer = 200000000
    queue = deque()
    for i, s in enumerate(stones):
        while queue and queue[-1] < s:
            queue.pop()
        while queue and i-k >= 0 and queue[0] > i - k:
            queue.pop()

        queue.append(s)
        if k <= i:
            answer = min(answer, queue[0])

    return answer

res = solution([7, 2, 8, 7,5, 2, 9], 3)
print(res)