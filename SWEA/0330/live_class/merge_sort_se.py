def msort(s, e):
    if s == e:
        return
    m = (s+e) //2
    msort(s, m)
    msort(m+1, e)

    k = 0
    l, r = s, m+1   # 왼쪽, 오른쪽에서 가장 작은 숫자의 위치
    while l =< m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1

        elif l <= m:
            while


    return merge()

N = int(input())
arr = list(map(int, input().split()))

msort(arr)