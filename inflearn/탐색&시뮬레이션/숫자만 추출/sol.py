import sys
sys.stdin = open('input.txt')

word = input()

num = ''
for str in word:
    if str.isdecimal():
        num += str
num = int(num)
print(num)

cnt = 0
for n in range(1, num+1):
    if num % n == 0:
        cnt += 1
print(cnt)

