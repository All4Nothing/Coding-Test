s = input()
stack = []
tmp = 1
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        tmp *= 2
    elif s[i] == '[':
        stack.append('[')
        tmp *= 3
    elif s[i] == ')':
        if s[i-1] == '(':
            answer += tmp    
        if not stack or stack[-1] == '[':
            answer = 0
            break
        stack.pop()
        tmp /= 2
    elif s[i] == ']':
        if s[i-1] == '[':
            answer += tmp
        if not stack or stack[-1] == '(':
            answer = 0
            break
        stack.pop()
        tmp /= 3
if stack:
    print(0)
else:
    print(int(answer))