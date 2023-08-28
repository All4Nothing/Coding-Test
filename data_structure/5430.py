import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    is_reverse = 0
    flag = 1
    cm = input().strip()
    n = int(input())
    l = deque(input().strip()[1:-1].split(','))
    if n == 0:
        l = []
    for c in cm:
        if c == 'R':
            if l:
                is_reverse += 1
        else:
            if not len(l):
                flag = 0
                print('error')
                break
            else:
                if is_reverse % 2 == 0:
                    l.popleft()
                else:
                    l.pop()
    if flag:
        l = list(l)
        if is_reverse % 2 == 0:
            print("[" + ",".join(l) + "]")
        else:
            l.reverse()
            print("[" + ",".join(l) + "]")