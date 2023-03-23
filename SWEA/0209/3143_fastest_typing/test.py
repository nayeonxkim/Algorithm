import sys
sys.stdin = open("input.txt")


def matching(target,pattern):
    target_l = len(target)
    pattern_l = len(pattern)
    count = 0
    i = 0
    j = 0
    while i < target_l:
        if target[i] == pattern[j]:
            j += 1
        else:
            j = 0
        if j == pattern_l:
            count += 1
            j = 0
        i += 1
    return count


T = int(input())
for tc in range(1,T+1):
    s1 , s2 = input().split()
    a = matching(s1,s2)
    ans = len(s1) - matching(s1,s2)*(len(s2)-1)
    print(f'#{tc} {a}')