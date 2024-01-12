import sys
sys.stdin = open('input.txt')

N = int(input())
target = int(input())

arr =[[0] * N for _ in range(N)]

di = [-1, 0, -1, 0]
dj = [0, 1, 0, -1]

i, j = 0, 0
num = N * N
turn = 0
arr[i][j] = num
ans = i+1, j+1
while num != 1:

    turn %= 4
    if turn == 0:
        while i <= N-2:
            num -= 1
            if arr[i+1][j] == 0:
                i += 1
                arr[i][j] = num
                if num == target:
                    ans = (i+1, j+1)
            else:
                num += 1
                break

    elif turn == 1:
        while j <= N-2:
            num -= 1
            if arr[i][j+1] == 0:
                j += 1
                arr[i][j] = num
                if num == target:
                    ans = (i + 1, j + 1)
            else:
                num += 1
                break

    elif turn == 2:
        while i >= 1:
            num -= 1
            if arr[i-1][j] == 0:
                i -= 1
                arr[i][j] = num
                if num == target:
                    ans = (i+1, j+1)
            else:
                num += 1
                break

    elif turn == 3:
        while j >= 1:
            num -= 1
            if arr[i][j-1] == 0:
                j -= 1
                arr[i][j] = num
                if num == target:
                    ans = (i+1, j+1)
            else:
                num += 1
                break


    turn += 1

for lst in arr:
    print(*lst)

print(*ans)




'''
0, 0부터 시작해서 
turn %= 4
num -= 1,

0
1) i가 N-1보다 작같, i+1칸에 값이 없으면
i += 1씩하면서 채움 

1
2) j가 N-1보다 작같, j+1칸에 값이 없으면
j += 1씩하면서 채움

2
3) i가 0보다 크거나 같, i-1칸에 값이 없으면
i -= 1씩하면서 채움

3
4) j가 i가 0보다 크거나 같, j-1칸에 값이 없으면
j -=1씩 하면서 채움

-> turn += 1

'''