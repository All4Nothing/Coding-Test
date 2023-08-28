import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = input().strip()
    pw = []
    sub = []
    for c in l:
        match c:
            case '<':
                if pw:
                    sub.append(pw.pop())
            case '>':
                if sub:
                    pw.append(sub.pop())
            case '-':
                if pw:
                    pw.pop()
            case _:
                pw.append(c)
    print(*pw, *sub[::-1], sep = '')