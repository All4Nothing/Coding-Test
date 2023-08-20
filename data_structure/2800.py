import sys
input = sys.stdin.readline
from itertools import combinations

s = input().rstrip()
stack = []
arr = []
answer = []

for idx, item in enumerate(s):
  if item == '(':
    stack.append(idx)
  if item == ')':
    start = stack.pop()
    arr.append([start, idx])
for i in range(1, len(arr)+1):
    comb = combinations(arr, i)
    for j in comb:
        tmp = list(s)
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.append(''.join(tmp))
print(*sorted(list(set(answer))), sep="\n")