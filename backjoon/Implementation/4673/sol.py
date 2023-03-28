'''
5
1~4중에 5가 되는 수가 있나?
있으면 break
끝까지 확인했는데 없으면 print(5)



'''

def d(num):
    res = 0
    while num != 0:
        res += num%10
        num //= 10
    return res


ans = [True] * 10001
for i in range(1, 10001):
    if i == d(i):
        ans[i] = False


for n in range(10001):
    if ans[n]:
        print(n)