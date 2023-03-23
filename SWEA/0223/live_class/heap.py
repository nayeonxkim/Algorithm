# 최대 100개의 key
# 최대 힙 = 부모 > 자식


def enq(n):
    global last

    # 완전이진트리에 정점 추가
    last += 1
    # 마지막 정점(last)에 숫자를 인큐한다.
    heap[last] = n

    c = last     # 마지막 정점을 자식노드로 두고
    p = c//2     # 완전이진트리이므로 단순히 나누기 2를 해서 부모노드를 구한다.

    # 부모가 있고, key값이 부모 < 자식이면 자리를 바꾼다.
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
    return


def deq():

    global last
    # 루트를 임시저장해둔다.
    tmp = heap[1]

    # 마지막 정점의 값을 루트로 이동
    heap[1] = heap[last]

    # 마지막 정점 삭제
    last -= 1

    # 현재 노드 = 루트 = 부모노드 없음
    # 나보다 큰 자식노드와 자리 바꾸기
    p = 1
    c = p * 2 # 왼쪽 자식 번호

    # 자식이 하나 이상 있으면
    while c <= last:
        # 오른쪽 자식노드가 있고, 오른쪽이 왼쪽보다 키가 크면
        # 비교대상을 오른쪽 자식노드로 변경
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        # 자식이 부모보다 크면 자리바꿈
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break

    return tmp









# 완전이진트리이므로 1~100번 인덱스 필요 (0번 인덱스는 사용하지 않는다.)
heap = [0] * 101
# heap = [0, 0, 0, ..., 0]에서 0번 인덱스가 현재 last
last = 0

enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])
# 확인해보면 가장 큰 값이 트리의 가장 위에있는 1 노드(root)에 위치 한다.

while last > 0:
    print(deq())