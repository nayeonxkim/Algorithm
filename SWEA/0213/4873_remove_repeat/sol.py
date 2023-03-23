import sys
sys.stdin = open('input.txt')

def search(word):
    # 문자가 같으면 다음 조사대상에 두 글자 모두 제외
    # 다르면 현재 조사대상 문자는 다음 조사에도 포함

    # 조사대상이되는 문자열을 만들어 word를 계속 업데이트함
    tmp = ''

    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            # 같으면 그 두개는 건너뛰고 저장
            tmp += word[i+2:]
            word = tmp
            i = 0
            tmp = ''
            print(word)
        else:
            # 다르면 그 단어도 조사대상에 포함
            tmp += word[i]
            i += 1
    return word

T = int(input())

for tc in range(1, T+1):
    word = input()
    print(len(search(word)))
