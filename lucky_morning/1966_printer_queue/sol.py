import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())

for _ in range(T):
    
    # input 받기 - 초기 인덱스가 따라다녀야하므로 enumerate 사용
    N, M = map(int, input().split())
    queue = deque(enumerate(map(int, input().split())))
    
    # 인쇄 횟수
    i = 0
    while queue:
        # 제일 큰 값의 인덱스 구하기
        max_element = max(queue, key=lambda x: x[1])
        max_idx = queue.index(max_element)
        
        # 해당 값의 앞 값까지 맨 위로 보내기
        # deque의 rotate으로
        queue.rotate(-max_idx)

        # deque의 popleft로
        # for _ in range(max_idx):
        #     queue.append(queue.popleft())
            
        # 0번으로 내려온 가장 큰 값 pop
        now_pop = queue.popleft()
        i += 1

        # 우리가 찾는 문서라면 인쇄 횟수 출력
        if now_pop[0] == M:
            print(i)
        

