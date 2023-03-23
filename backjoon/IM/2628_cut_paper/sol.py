import sys
sys.stdin = open('input.txt')

#
W, H = map(int, input().split())
width = []
height = []

L = int(input())
for _ in range(L):
    a, num = map(int, input().split())
    if a:
        height.append(num)
    else:
        width.append(num)
width.sort()
height.sort()
print(width, height)
# w, h = map(int,input().split())
# a = int(input())
# cut = []
# x = []
# y = []
# for i in range(a):
#     cut.append(input().split())
#     # print(list(cut))
#     if int(cut[i][0]) == 1:
#         x.append(int(cut[i][1]))
#         # print(list(x))
#     else:
#         y.append(int(cut[i][1]))
#
# X = sorted(x)
# Y = sorted(y)
#
# print(list(X))
# print(list(Y))
#
# w_set = []
# w_set.append(X[0])
# for j in range(len(X)-1):
#     w_set.append(int(X[j+1]) - int(X[j]))
# w_set.append(w - int(X[len(X)-1]))
#
# h_set = []
# h_set.append(Y[0])
# for k in range(len(Y)-1):
#     h_set.append(int(Y[k+1]) - int(Y[k]))
# h_set.append(h - int(Y[len(Y)-1]))
#
#
# print(list(w_set))
# print(list(h_set))
#
# result = max(w_set)*max(h_set)
#
# print(result)