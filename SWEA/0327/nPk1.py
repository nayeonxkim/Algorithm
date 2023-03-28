# i : 값을 결정할 자리, k : 결정할 개수
def perm(i, k):
    if i==k:
        print(*p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
