text = 'Today is Thursday'
pattern = 'day'

N = len(text)
M = len(pattern)

def BruteForce(p, t, lenOfPattern, lenOfText):
    i = j = 0
    cnt = 0
    for i in range(lenOfText-lenOfPattern+1):
       for j in range(lenOfPattern):
           # 다르면 j 반복문 종료 -> 다음 i로 이동해서 패턴의 처음(j=0)부터 다시 확인
           if t[i+j] != p[j]:
               break
           # 같으면 cnt에 1추가
           else:
               cnt += 1
    # 모든 반복문이 끝나고 패턴의 개수 반환
    return cnt


print(BruteForce(pattern, text, M, N))

# 그림그리면서 다시