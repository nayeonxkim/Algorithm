import sys
sys.stdin = open('input.txt',encoding = 'UTF-8')


def search(pattern, char):
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] == char:
            return len(pattern) - i - 1
    # 해당 글자가 패턴안에 없으면
    return len(pattern)



def boyer_moore(pattern, text):
    cnt = t_idx = 0

    # 텍스트 길이 - 패턴 길이를 벗어나지 않을때까지만 조사
    while t_idx <= len(text) - len(pattern):

        # 뒤에서부터 조사
        p_idx = len(pattern) - 1
        # pattern의 범위를 벗어나지 않을 때까지만 조사
        while p_idx >= 0:
            # 두 글자가 같지 않다면
            if pattern[p_idx] != text[t_idx + p_idx]:
                next = search(pattern, text[t_idx + len(pattern) -1])
                break
            # 같으면 패턴의 한칸 앞글자와 비교
            p_idx -= 1
        # 패턴의 처음까지 모두 조사했다면
        if p_idx == -1:
            cnt += 1
            t_idx += 1
        else:
            t_idx += next
    return cnt



for _ in range(10):
    tc = int(input())
    pattern = input()
    text = input()
    print(boyer_moore(pattern, text))