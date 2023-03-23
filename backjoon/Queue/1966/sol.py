<<<<<<< HEAD
=======
'''
1. 리스트 enumarate로 받기 : 인덱스 붙여서 쌍으로 확인
6개, 확인하고 싶은 문서 = 0번 문서
"0, 1" (1, 1) (2, 9) (3, 1) (4, 1) (5, 1)
(1, 1) (2, 9) (3, 1) (4, 1) (5, 1) "0, 1"
(2, 9) (3, 1) (4, 1) (5, 1) "0, 1" (1, 1)

2. queue[0][1]이 다른 모든 queue[i][1]보다 큰지 확인
cnt = 0
- for문?
- max?

있다
    : queue.append(queue.pop(0))
없다
    : cnt += 1
    if queue[0][0] == M:
        break
    else:
        queue.pop(0)

'''

>>>>>>> 174df9aaff211f8c77331a226a2fa68a26b561ca
import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
<<<<<<< HEAD
    arr =
=======
    queue = list(enumerate(map(int, input().split())))
    print(queue)

    print(max(queue))

>>>>>>> 174df9aaff211f8c77331a226a2fa68a26b561ca
