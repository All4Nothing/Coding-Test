import sys
input = sys.stdin.readline
n = int(input())
top = list(map(int, input().split()))
answer = [0] * n
stack = []
for i in range(n):
    while len(stack):
        if stack[-1][1] < top[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,top[i]))
print(*answer)