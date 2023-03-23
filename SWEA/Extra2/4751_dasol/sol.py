import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    word = input()

    first = '..' + '...'.join('#'*len(word)) + '..'
    second = '.'+'.'.join('#'*len(word)*2)+'.'
    third = '#.'+ '.#.'.join(i for i in word)+'.#'
    print(f'{first}\n{second}\n{third}\n{second}\n{first}')