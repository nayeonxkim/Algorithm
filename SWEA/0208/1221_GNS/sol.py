import sys
sys.stdin = open('input.txt')

# 외계 숫자 리스트 생성 : 인덱스 = 해당 글자를 뜻하는 숫자
alien_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    print(tc)

    # num 리스트를 입력받는다.
    num = list(input().split())

    # 버블 정렬
    for n in range(N-1, 0, -1):
        for i in range(n):
            # 외계 숫자 리스트에서의 글자 num의 인덱스값을 비교. 글자 = 인덱스
            if alien_num.index(num[i]) > alien_num.index(num[i+1]):
                num[i], num[i+1] = num[i+1], num[i]



    print(*num)

