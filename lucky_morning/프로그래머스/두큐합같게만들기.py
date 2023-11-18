from collections import deque


def solution(queue1, queue2):
    answer = 0

    tot1 = sum(queue1)
    tot2 = sum(queue2)

    if (tot1 + tot2) % 2 != 0:
        return -1

    # 두 큐에 모두 값이 있다면 작업 수행
    while queue1 and queue2:
        # 두 합이 같으면 작업 끝
        if tot1 == tot2:
            return answer

        # 큐1의 합이 더 크다면, 큐1 -> 큐2
        elif tot1 > tot2:
            num = queue1.pop(0)
            queue2.append(num)
            tot1 -= num
            tot2 += num

        # 큐2의 합이 더 크다면, 큐2 -> 큐1
        else:
            num = queue2.pop(0)
            queue1.append(num)
            tot2 -= num
            tot1 += num

        answer += 1

    return -1

