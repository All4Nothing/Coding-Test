from collections import deque
import sys
input = sys.stdin.readline

q = deque([])

for _ in range(int(input())):
    inp = input().split()
    match inp[0]:
        case 'push':
            q.append(inp[1])
        case 'pop':
            print(q.popleft()) if q else print(-1)
        case 'size':
            print(len(q))
        case 'empty':
            print(0) if q else print(1)
        case 'front':
            print(q[0]) if q else print(-1)
        case 'back':
            print(q[-1]) if q else print(-1)