from collections import deque
import sys
input = sys.stdin.readline

input()
b = deque(enumerate(map(int, input().split())))
while b:
    indx, num = b.popleft()
    b.rotate(-num+1 if num>0 else -num)
    print(indx+1, end=" ")