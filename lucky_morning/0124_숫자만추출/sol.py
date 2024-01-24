import sys
sys.stdin = open('input.txt')

word = input()

# 자연수 만들기
num = ''
for char in word:
    if char.isdecimal():
        num += char
num = int(num)

# 약수의 개수 구하기
cnt = 0
for n in range(1, num+1):
    if num % n == 0:
        cnt += 1

# 출력하기
print(num)
print(cnt)