'''

입력
3
400 300 350
1000 299 578
1000 222 888

출력
#1 A
#2 0
#3 A
---

이진 탐색한 횟수 구하기

end, key

1~end에서 middle 찾음
반복문 한번 할 때마다 cnt += 1
middle이 key랑 같으면 끝 !
middle이 키보다 크면 시작지점이 middle
middle이 key보다 작으면 끝지점이 middle

'''


import sys
sys.stdin = open('input.txt')

# 이진검색 함수 정의
def binarysearch(page, key):

    # 검색구간의 첫 페이지와 마지막 페이지 설정
    cnt = 0
    start = 1
    end = page

    # 첫 페이지가 마지막 페이지보다 커지면 반복문 종료 : 더이상 검색할 수 있는 구간 없다는 뜻
    while start <= end:
        # 가운데 값 구함
        middle = int((start+end)/2)
        # 반복문 한 번 돌아갈 때마다 횟수 +1
        cnt += 1
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle
    return cnt


T = int(input())

for tc in range(1, T+1):
    page, A, B = map(int, input().split())

    # A와 B 각각을 함수에 넣고 계산하여 이긴 사람 반환, 비기면 0
    if binarysearch(page, A) > binarysearch(page, B):
        ans = 'B'
    elif binarysearch(page, A) < binarysearch(page, B):
        ans = 'A'
    else:
        ans = '0'

    print(f'#{tc} {ans}')


