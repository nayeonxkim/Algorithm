'''
## 덤프만큼 반복 : while
# 높이 리스트를 정렬한다.
카운팅 정렬, 버블 정렬
[오름차순 정렬된 높이 리스트]
덤프만큼이 끝나면 여기서 break

# 리스트의 첫 값은 +1, 마지막 값은 -1
[덤프 1회가 끝난 높이 리스트]

# while문 끝나면 리스트 마지막 요소 - 첫 요소
값
'''

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    i = 0
    while i < dump:
        # 카운팅 정렬
        cnt = [0] * 101
        for n in heights:
            cnt[n] += 1
