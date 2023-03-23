import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    text = input()

    cnt = i = j = 0
    while j < len(text):
        if text[i] == pattern[j]:
            j += 1
        else:
            i += 1
            j = 0
        if j == len(pattern):
            cnt += 1


    print(cnt)