'''
## 입력받는다.
[5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]

1st dump

## 덤프 횟수만큼 반복한다.
# i = 0
# i < dump 반복
# 가장 큰 수 max 구하기
# 가장 작은 수 min 구하기
# max - 1, min + 1
[5, 8, 3, **2**, 5, 6, **8**, 9, 2, 2, 4]

2nd dump

[5, 8, 3, 2, 5, 6, 8, **8**, **3**, 2, 4]

# 끝나면 card 출력

## dump 끝난 후의 max, min구하기
dump completed
[5, 8, 3, 2, 5, 6, 8, 8, 3, 2, 4]
8 - 6 = 2

'''
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    # 지정된 덤프 횟수만큼 반복
    # 가장 큰 높이는 -1, 가장 낮은 높이는 +1
    i = 0
    while i < dump:
       max_idx = heights.index(max(heights))
       min_idx = heights.index(min(heights))

       heights[max_idx] -= 1
       heights[min_idx] += 1
       i += 1

    print(f'#{tc} {max(heights) - min(heights)}')

