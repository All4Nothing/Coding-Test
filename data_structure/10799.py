cnt = 0
inp = input()
stack = []

for i in range(len(inp)):
    if inp[i] == '(':
        stack.append('(')
    else:
        if inp[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)