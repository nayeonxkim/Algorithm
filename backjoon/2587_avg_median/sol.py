import sys
sys.stdin = open('input.txt')

numbers = [0] * 5
total = n = 0

for i in range(5):
    numbers[i] = int(input())

# 평균
    total += numbers[i]
    n += 1

print(int(total/n))

# 중앙값
## 선택 정렬
for i in range(4):
    minIdx = i
    for j in range(i+1, 5):
        if numbers[minIdx] > numbers[j]:
            minIdx = j
    numbers[i], numbers[minIdx] = numbers[minIdx], numbers[i]

print(numbers[2])