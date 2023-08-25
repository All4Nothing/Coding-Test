import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
com = list(map(int, input().split()))
l = deque()
for i in range(1, n+1):
    match com.pop():
        case 1:
            l.appendleft(i)
        case 2:
            l.insert(1,i)
        case 3:
            l.append(i)
print(*l)