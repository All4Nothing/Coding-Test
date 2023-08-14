import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
n_list = deque([i for i in range(1, n+1)])
print('<', end='')
while len(n_list) > 1:
    n_list.rotate(-k+1)
    print(n_list.popleft(),end=', ')
print(*n_list, '>', sep='')