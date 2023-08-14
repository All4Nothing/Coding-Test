import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
n_list = deque([i for i in range(1, n+1)])
l=['<']
while len(n_list):
    n_list.rotate(-k+1)
    l.append(n_list.popleft())
    l.append(', ')
print(*l[:-1],'>', sep='')