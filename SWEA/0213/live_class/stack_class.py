# 스택 클래스 생성
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.top = -1

    # 빈 스택인지 확인하는 메서드
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 값을 추가하는 메서드
    def push(self, item):
        if self.is_full():
            print('Full_Stack : can not push')
        else:
            self.top += 1
            self.items[self.top] = item

    # 현재 top의 값을 반환하는 메서드
    # 스택이 비었다면 ? 오류를 발생시킨다.
    def peek(self):
        if self.is_empty():
            raise Exception('Empty_Stack')
        else:
            return self.items[self.top]

    # 값을 제거하는 메서드
    def pop(self, item):
        self.items[self.top]

    # 스택에 값이 다 찼는지 확인하는 메서드
    def is_full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    # 값을 제거하는 메서드
    def pop(self):
        if self.is_empty():
            print('Empty_Stack : can not pop')
        else:
            # top에 있는 (가장 마지막) 값을 반환하고
            # top을 한칸 내린다.
            value = self.items[self.top]
            self.top -= 1
            return value
            # items에는 value가 아직 존재함!
            # 그러나 스택은 top을 기준으로 삽입/삭제하기 때문에 상관 X
            # 사실상 진짜 삭제한다기 보다 top을 내려서 덮어쓸 수 있게끔 하는 것

s1 = Stack(5)

s1.push('A')
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('E')

print(s1.items)
print(s1.peek())
print(s1.is_full())