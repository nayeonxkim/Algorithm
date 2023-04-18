'''
1. 문자열 오름차순
2. 모음 1개, 자음 2개 필수
3. 총 C개의 문자 중 L개로 만듦
'''
import sys
sys.stdin = open('input.txt')

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

def promising(word):

    v = c = 0
    # 모음이 한개, 자음이 두개
    vowels = 'aeiou'

    for char in word:
        if char in vowels:
            v += 1
        else:
            c += 1

    if v >= 1 and c >= 2:
        return 1
    else:
        return 0

def backtrack(i, L, C, arr, ans):

    # 종료조건
    if len(ans) == L:
        # 가능성 검사
        if promising(ans):
            print(ans)
        return

    # 종료조건
    if i == C:
        return

    backtrack(i + 1, L, C, arr, ans + arr[i])
    backtrack(i + 1, L, C, arr, ans)

backtrack(0, L, C, arr, '')
