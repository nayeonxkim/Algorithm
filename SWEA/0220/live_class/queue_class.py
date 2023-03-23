class Queue:
    def __init__(self, n):
        self.size = n   # 큐의 전체 크기
        self.items = [None] * n
        self.rear = -1  # 값을 넣는 위치
        self.front = -1 # 값을 빼는 위치

    def enQueue(self, item):
        if self.isFull():
            print('큐가 꽉 찼어염')
        else:
            self.rear += 1
            self.items[self.rear] = item
            # 해당 자리에 item을 넣어준다.

    def deQueue(self):
        if self.isEmpty():
            print('큐가 비었어염')
        else:
            self.front += 1
            # 반환을 위해 뺄 값을 None으로 바꾸기 전에 item 변수에 저장해둠
            item = self.items[self.front]
            self.items[self.front] = None
            return item

    def isEmpty(self):
        return self.front == self.rear
        # 두 위치가 같다면 해당 큐는 비어있는 것

    def isFull(self):
        return self.rear == self.size -1
        # rear가 전체 큐의 마지막 위치에 있으면 해당 큐는 꽉 찬 것

# 큐 생성하기
q = Queue(4)
print(q.items)

# 큐에 값 삽입하기
q.enQueue('A')
q.enQueue('B')
print(q.items)
print(q.rear)
print(q.front)

# 큐에서 값 삭제하기
print(q.deQueue())
print(q.items)
print(q.rear)
print(q.front)
# items에는 변화가 없어보이지만 front의 값이 변한 것을 확인할 수 있다.
# -1 -> 0 하나 삭제해서 오른쪽으로 한 칸 땡겨짐

# 선형 큐 -> 잘못된 포화상태 인식
