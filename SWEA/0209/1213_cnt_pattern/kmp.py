import sys
sys.stdin = open('input.txt')

# 패턴 내에 패턴이 존재하는지 확인하고, 해당 정보를 담는 리스트를 생성하는 함수
def make_lps(pattern):
    lps = [0] * len(pattern)

    lps_idx = 0
    for i in range(1, len(pattern)):
        # 지금 조사하는 글자와 그 이전의 글자가 같다면
        if pattern[lps_idx] == pattern[i]:
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:
            # 두 글자가 서로 다르면 0으로 초기화시켜서 패턴의 0번째와 다시 비교한다.
            lps_idx = 0
            if pattern[i] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1

    return lps

def KMP(pattern, text):
    lps = make_lps(pattern)

    p_idx = t_idx = cnt = 0
    while t_idx < len(text):
        if pattern[p_idx] == text[t_idx]:
            t_idx += 1
            p_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx - 1]

        if p_idx == len(pattern):
            cnt += 1
            p_idx = 0
    return  cnt