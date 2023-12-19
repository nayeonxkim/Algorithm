import sys
sys.stdin = open('input.txt')
from collections import deque
'''
큐 풀이
필수과목 = 큐
1. plan의 한 과목씩 순회하며 검사
2. 현재 과목이 큐의 첫번째 과목과 일치하지 않는다면 바로 NO 반환
3. 만약 순서대로 일치하여 for문이 끝난다면 큐의 길이를 확인
4. 큐의 길이가 0이라면 모든 필수과목이 설계 된 상태 -> YES 반환
5. 큐의 길이가 1이상이라면 하나 이상의 필수과목이 설계되지 않음 -> NO 반환

** 필수과목이 두 번 나오는 경우도 순서만 일치한다면 YES를 반환해야하는데, NO를 반환하지 않나?
큐를 사용하여 풀이하므로, 한 번 나온 과목은 popleft하여 큐에서 사라진 상태
따라서 한 과목이 두 번째 나오면 이는 필수과목에 포함되지 않는 과목이라고 여겨짐
따라서 문제없이 YES를 반환함
=> 각 필수과목에 대해 단 한 번씩만 순서를 검사한다고 생각하면 됨
'''

need = input()
N = int(input())
for tc in range(1, N+1):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("NO")
    else:
        if len(dq) == 0:
            print("YES")
        else:
            print("NO")