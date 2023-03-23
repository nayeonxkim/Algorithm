text = 'Thursday is'
pattern = 'is'

N = len(text)
M = len(pattern)

def BruteForce(p, t, lenOfPattern, lenOfText):
    i = j = 0
    # 패턴의 범위를 벗어나거나, 텍스트의 범위를 벗어나면 반복문 종료
    # 조건에 맞게 이동하여 계속 다시 비교
    while j < lenOfPattern and i < lenOfText:
        # 만약 텍스트가 패턴과 일치한다면
        # 텍스트와 패턴 모두 한칸씩 이동
        if t[i] == p[j]:
            i += 1
            j += 1
        # 일치하지 않는다면
        else:
            # 텍스트는 처음 출발한 위치 한칸 뒤로 이동
            # 패턴은 가장 처음으로 이동
            i = i - j + 1
            j = 0
    # j이동 위치가 패턴길이와 일치한다면
    # -> 텍스트와 패턴이 일치하지 않으면 j는 0으로 다시 돌아간다.
    # -> 즉, j의 위치가 패턴의 총 길이와 같다면 텍스트에서 패턴의 길이만큼 일치하는 문자를 찾았다는 뜻
    # 따라서 j == M은 패턴을 찾았다는 뜻.
    if j == lenOfPattern:
        return i
    # j가 M이 아닌데 반복문이 종료되었다면, i가 N을 벗어난 것
    # 즉 텍스트를 다 돌때까지 j가 M과 같아지는 경우가 없었다는 것
    else:
        return -1

print(BruteForce(pattern, text, M, N))
# 확인할 케이스
# 1.가장 처음에 패턴이 있는 경우
# 2.제일 마지막에 패턴이 있는 경우
# 3.패턴이 없는 경우