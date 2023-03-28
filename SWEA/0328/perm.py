def perm(depth, r):
    # depth:현재까지 조사한 대상의 수
    # r : 총 조사할 대상의 개수
    if depth == r:
        print(check)
    # check에 아직 r개 만큼 값이 채워지지 않은 경우
    else:
        # nums의 모든 대상을 조사
        for i in range(len(nums)):
            # nums의 i번째를 아직 사용한 적 없다면
            if not visited[i]:
                visited[i] = True # 사용표시하고
                check[depth] = nums[i] # check의 depth번째에 nums[i]를 넣는다.
                perm(depth+1, r) # 하나 조사했으니 depth에 +1, 전체 조사대상은 변하지않으므로 그대로 r
                visited[i] = False # 썼던거 다시 사용표시 없애기

nums = [1,2,3]
visited = [0] * 3
check = [0] * 2
perm(0, 2)