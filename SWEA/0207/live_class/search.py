# 정렬되지 않은 경우
A = [1, 5, 63, 2, 8, 92, 3]

def sequentialSearch(a, n, key):
    # 0번 인덱스부터 검색할거야
    i = 0
    # 내가 찾는 값이 a의 i번째에 없고, i가 a의 범위(n)를 벗어나지 않을 때까지
    # *항상 인덱스의 유효범위를 먼저 확인하기*
    while i < n and a[i] != key:
        # i를 뒤로 한 칸씩 이동해
        i += 1
    # while문의 조건문과 반대되면 while문 건너뛰고 아래 코드 실행
    # i가 a의 범위 안에 있다면, 해당 값이 a에 있어서 중단된것. : a[i]가 key와 같다.
    if i < n:
        # 따라서 해당 인덱스를 반환한다.
        return i
    # i가 a의 범위를 벗어났다면, a에서 해당 값을 찾지 못한 것. : i가 a의 범위를 벗어날 때까지 찾지 못했다.
    else:
        # 따라서 -1을 반환한다.
        return -1

print(sequentialSearch(A, len(A), 8))
print(sequentialSearch(A, len(A), 7))

# 정렬되어 있는 경우
B = [3, 5, 8, 13, 35, 78, 102]

def sequentialSearch2(a, n, key):
    i = 0
    # a에서 내가 찾는 값보다 작은 값들만, i가 a의 범위를 벗어나지 않을 때까지
    # 왜 <=가 아닌 <?
    # 같으면 찾았기 때문에 중단되어야함.
    while i < n and a[i] < key:
        # i를 하나씩 커지게 하면서 순회한다.
        i += 1
    # 만약 a안에서  key값을 찾는다면
    if i < n and a[i] == key:
        # i값을 반환한다.
        return i
    # i가 a의 범위를 벗어나거나, a[i]가 key보다 커지면
    else:
        # 검색실패를 반환한다.
        return -1

print(sequentialSearch2(B,len(B), 35))
print(sequentialSearch2(B,len(B), 123))
print(sequentialSearch2(B,len(B), 22))
