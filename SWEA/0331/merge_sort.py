def msort(s, e):
    # 시작 = 끝 인덱스이면 한 칸인거니까 그만 쪼개기
    if s == e:
        return

    m = (s+e)//2
    msort(s, m)
    msort(m+1, e)

    # 두 그룹에서 가장 작은 수 뽑아냄
    k = 0 # tmp에 값을 넣을 위치
    l = s
    r = m+1
    # 두 값이 범위 내에 있으면 아직 비교할 값이 남아있다는 뜻
    while l <= m or r <= e:

        # 둘 다 내부에 있으면 비교해서 작은 값 tmp에 넣기
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1

        # 왼쪽 그룹만 값이 남아있다면, 그냥냥
        elif l<= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1

        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1
