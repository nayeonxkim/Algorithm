import sys
sys.stdin = open('input.txt')

N = int(input())
n_lst = list(map(int, input().split()))

M = int(input())
m_lst = list(map(int, input().split()))

p1 = p2 = 0
lst = []
while p1 < N and p2 < M:
    if n_lst[p1] < m_lst[p2]:
        lst.append(n_lst[p1])
        p1 += 1
    elif n_lst[p1] > m_lst[p2]:
        lst.append(m_lst[p2])
        p2 += 1
    else:
        lst.append(n_lst[p1])
        lst.append(m_lst[p2])
        p1 += 1
        p2 += 1
print(lst)

