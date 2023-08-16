import sys
input = sys.stdin.readline
from collections import deque

q = deque([])

for _ in range(int(input())):
    arr = list(input().split())
    match arr[0]:
        case 'push':
            q.append(arr[1])
        case 'pop':
            if len(q):
                print(q.popleft())
            else:
                print(-1)
        case 'size':
            print(len(q))
        case 'empty':
            if len(q):
                print(0)
            else:
                print(1)
        case 'front':
            if len(q):
                print(q[0])
            else:
                print(-1)
        case 'back':
            if len(q):
                print(q[-1])
            else:
                print(-1)