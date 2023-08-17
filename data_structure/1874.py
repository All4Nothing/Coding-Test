import sys
# input = sys.stdin.readline
from collections import deque

arr=[]
i=1
answer = []
for _ in range(int(input())):
    num = int(input())
    while i <= num:
      arr.append(i)
      answer.append('+')
      i += 1
    if arr[-1] == num:
      arr.pop()
      answer.append('-')
    else:
      print('NO')
      break
if not len(arr):
  print(*answer, sep="\n")