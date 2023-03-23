'''
---
# 1. 거꾸로 뒤집은 리스트 만들기
# 2. 두 리스트의 내용이 똑같으면 1, 다르면 0
---

# 1. 리스트 거꾸로 뒤집기
reversed  4 -> 3 -> 2 -> 1 -> 0
word      0 -> 1 -> 2 -> 3 -> 4

# 내용이 같은지 확인 : ==
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = list(input())

    # 뒤집은 리스트
    reversed_word = [''] * len(word)
    for i in range(len(word)):
        j = len(word) - 1 - i
        reversed_word[j] = word[i]

    # 두 리스트가 같은지 확인하기
    if word == reversed_word:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')