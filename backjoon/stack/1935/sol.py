
'''

ABC*+DE/-

123*+45/-

int

A = 1
B = 2
뒷 숫자가 앞에온다

'''
import sys
sys.stdin = open('input.txt')

N = int(input())
cal = input()

for i in range(65, 65+N):
    cal = cal.replace(chr(i), input())
print(cal)

stack = []
for char in cal:
    if char not in '*/+-':
        stack.append(int(char))
    elif char == '+':
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(n1 + n2)
    elif char == '-':
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(n1 - n2)
    elif char == '*':
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(n1 * n2)
    elif char == '/':
        n2 = stack.pop()
        n1 = stack.pop()
        stack.append(n1 / n2)

print(f'{stack[-1]:0.2f}')