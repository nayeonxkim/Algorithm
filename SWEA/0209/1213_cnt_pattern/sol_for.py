import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    text = input()
    cnt = 0

    for t_idx in range(len(text)-len(pattern)+1):
        for p_idx in range(len(pattern)):
            if pattern[p_idx] != text[t_idx + p_idx]:
                break
        # for문의 else. break되지 않고 반복문을 모두 순회하면 else문 실행
        else:
            cnt += 1
    print(cnt, text.count(pattern))
