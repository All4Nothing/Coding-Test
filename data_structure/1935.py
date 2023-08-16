import sys
input = sys.stdin.readline

n = int(input())
exp = input().strip()
alpha = []
stack = []
for i in range(n):
    alpha.append(int(input()))
for i in exp:
    if 'A' <= i <= 'Z':
        stack.append(alpha[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        match i:
            case '*':
                stack.append(str1 * str2)
            case '/':
                stack.append(str1 / str2)
            case '+':
                stack.append(str1 + str2)
            case '-':
                stack.append(str1 - str2)
print("%.2f" %stack[0])