def solution(new_id):
    answer = ''

    # 1. 소문자 치환
    new_id = list(new_id.lower())

    # 2. 글자 제거
    remove_lst = []
    for char in new_id:
        if char not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            remove_lst.append(char)
    for char in remove_lst:
        new_id.remove(char)

    # 3. 2번 연속 . 하나로
    new_id = ''.join(new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4. 처음과 끝 마침표 제거
    if new_id[0] == '.':
        new_id = new_id[1:]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5. 빈 문자열이면 a 대입
    if new_id == '':
        new_id = 'a'

    # 6. 첫 15개만 남기고 마지막 마침표 제거
    new_id = new_id[:15]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]

    # 7. 2자 이하라면 마지막 글자를 3이 될 때까지 반복
    while len(new_id) <= 2:
        new_id += new_id[-1:]

    answer = new_id
    return answer