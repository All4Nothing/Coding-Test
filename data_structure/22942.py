import sys
input = sys.stdin.readline
circles = []
stack = []
for i in range(int(input())):
    c, r = map(int, input().split())
    circles.append((c-r, i))
    circles.append((c+r, i))
circles.sort()
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)
print('NO') if stack else print('YES')