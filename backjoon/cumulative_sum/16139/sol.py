import sys
sys.stdin = open('input.txt')

S = sys.stdin.readline()
res = list([''] * (len(S)+1))

for i in range(len(S)):
    res[i+1] = S[i] + res[i]
q = int(sys.stdin.readline())

for _ in range(q):
    alpha, l, r = sys.stdin.readline().split()
    l, r = int(l)+1, int(r)+1
    ans = res[r].count(alpha) - res[l-1].count(alpha)
    print(ans)