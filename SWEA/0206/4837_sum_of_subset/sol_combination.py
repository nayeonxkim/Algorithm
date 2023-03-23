from itertools import combinations

T = int(input()) # tc


# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 해당하는 부분집합이 없는 경우 0

nums = {x for x in range(1, 13)}

for tc in range(1, T+1):
    N, K = map(int, input().split()) #부분집합 원소수 N 부분집합 합 K
    cnt = 0
    for j in combinations(nums, N):
        if sum(j) == K:
            cnt += 1

    print(f'#{tc} {cnt}')