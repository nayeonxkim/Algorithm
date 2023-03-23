import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text, pattern = input().split()
    # banana -> Ona
    # 패턴과 일치하면 해당 문자들을 'O'로 바꾸어주기 위해 리스트로 변환 : 문자열을 바꿀 수 없어요
    t_lst, p_lst = list(text), list(pattern)

    # banana ba
    # 텍스트가 패턴보다 길거나 같을 때 까지만 : 패턴길이만큼 묶어서 비교하기 때문에 패턴보다 짧아지면 안된다.
    while len(t_lst) >= len(p_lst):
        for i in range(len(t_lst)-len(p_lst)+1):
            # 텍스트를 패턴 길이만큼 묶어서 패턴과 같으면 해당 문자들을 'O'로 바꾸어줍니다.
            if t_lst[i:i+len(p_lst)] == p_lst:
                t_lst[i:i + len(p_lst)] = 'O'
        # 모든 텍스트 덩어리에 대해 확인을 끝내면 for문을 종료한다.
        # 확인을 다했는데 없으면 안잘려서 길이가 안줄어드니까
        break
    print(t_lst)
    print(f'#{tc} {len(t_lst)}')


