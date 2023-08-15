from collections import deque
import sys
input = sys.stdin.readline

arr = deque([])
for _ in range(int(input())):
    inp = input().split()
    match inp[0]:
        case 'push_front':
            arr.appendleft(int(inp[1]))
        case 'push_back':
            arr.append(int(inp[1]))
        case 'pop_front':
            print(arr.popleft()) if len(arr) else print(-1)
        case 'pop_back':
            print(arr.pop()) if len(arr) else print(-1)
        case 'size':
            print(len(arr))
        case 'empty':
            print(0) if len(arr) else print(1)
        case 'front':
            print(arr[0]) if len(arr) else print(-1)
        case 'back':
            print(arr[-1]) if len(arr) else print(-1)