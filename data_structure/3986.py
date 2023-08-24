cnt = 0
for _ in range(int(input())):
    l = input()
    stack = []
    for i in l:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        cnt += 1
print(cnt)