import sys
sys.stdin = open('input.txt')
from itertools import permutations
'''

1, 2, 3

123 중 수열의 마지막 수를 뺸 둘 중 하나
1 -> 2, 3중에 하나
12 -> 1, 3 중에 하나
121 -> 2, 3 중에 하나
1212 -> X
1213 
'''
