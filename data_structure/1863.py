stack = []
skylines = []
ans = 0
for _ in range(int(input())):
    _, y = map(int, input().split())
    while stack and stack[-1] > y:
        ans += 1
        stack.pop()
    if stack and stack[-1]==y:
        continue
    stack.append(y)
while stack:
    if stack[-1] > 0:
        ans += 1
    stack.pop()
print(ans)