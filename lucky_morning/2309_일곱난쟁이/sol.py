import sys
sys.stdin = open('input.txt')

lst = [int(input()) for _ in range(9)]

# 1. 아홉 난쟁이 중 빠져야할 난쟁이 2명 찾기
for i in range(9):
    for j in range(i+1, 9):
        if sum(lst) - lst[i] - lst[j] == 100:
            d1, d2 = lst[i], lst[j]

# 2. 찾은 두 명 리스트에서 제거
lst.remove(d1)
lst.remove(d2)

# 3. 오름차순 정렬
for i in range(7):
    for j in range(6-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

# 4. 하나씩 출력
for i in lst:
    print(i)