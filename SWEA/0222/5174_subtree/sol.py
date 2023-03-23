import sys
sys.stdin = open('input.txt')
# 전위순회

def preorder(node):
    # 전역변수 불러옴
    global cnt

    if node != 0:
        # 자식이 없을 때, 출력대신 cnt를 증가시킴
        cnt += 1
        preorder(left[node])
        preorder(right[node])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))

    # 왼쪽/오른쪽 자식노드
    left = [0] * (E+2)
    right = [0] * (E+2)

    # 짝수번은 부모노드, 홀수번은 자식노드로 입력받음
    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        
        # 왼쪽 자식이 없다면 왼쪽에 추가
        if left[p] == 0:
            left[p] = c
        # 있으면 오른쪽에 추가
        else:
            right[p] = c
    
    # 자신의 자식노드 수를 세어줄 cnt 변수
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')





