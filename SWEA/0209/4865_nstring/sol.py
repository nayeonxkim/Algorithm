import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()

    p = len(pattern)
    t = len(text)

# 패턴 : abs
# 텍스트 : adjsabbsa
    cnt = [0] * p
    for i in range(p):
        for j in range(t):
            if pattern[i] == text[j]:
                cnt[i] += 1

    print(f'#{tc} {max(cnt)}')