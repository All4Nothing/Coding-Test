#import sys
#input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    inp = input().split()
    match inp[0]:
        case 'push':
            stack.append(int(inp[1]))
        case 'pop':
            print(stack.pop()) if len(stack) else print(-1)
        case 'size':
            print(len(stack))
        case 'empty':
            print(0) if len(stack) else print(1)
        case 'top':
            print(stack[-1]) if len(stack) else print(-1)