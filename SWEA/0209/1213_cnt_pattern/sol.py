import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    text = input()

    # BruteForce
    p_idx = t_idx = 0
    # 패턴이 텍스트에 등장하는 횟수
    cnt = 0

    while t_idx < len(text):
        # 두 값이 같으면 인덱스 + 1
        if text[t_idx] == pattern[p_idx]:
            t_idx += 1
            p_idx += 1
        # 패턴의 모든 문자에 대해 조사를 마쳤다면
        if p_idx == len(pattern):
            cnt += 1
            p_idx = 0

        if text[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx + 1
            p_idx = 0

    print(pattern, text)