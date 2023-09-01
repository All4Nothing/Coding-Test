import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
arr = [[0,-1e9,-1] for i in range(n)]
arr2 = []
stack = []
stack2 = []
len1 = []
len2 = []
for idx, h in enumerate(l):
    if not stack:
        stack.append([idx,h])
    else:
        while stack and stack[-1][1] <= h:
            stack.pop()
        arr[idx][0] += len(stack)
        len1.append([idx,len(stack)])
        if stack:
            arr[idx][1] = stack[-1][0] + 1
        stack.append([idx, h])

for idx, h in reversed(list(enumerate(l))):
    if not stack2:
        stack2.append([idx,h])
    else:
        while stack2 and stack2[-1][1] <= h:
            stack2.pop()
        arr[idx][0] += len(stack2)
        len2.append([idx,len(stack2)])
        if stack2:
            arr[idx][2] = stack2[-1][0] + 1
        stack2.append([idx, h])

for idx, item in enumerate(arr):
    if abs(idx + 1 - item[1]) <= abs(idx + 1 - item[2]):
        num = item[1]
    else:
        num = item[2]
    if num > 0:
        arr2.append([item[0], num])
    else:
        arr2.append([item[0]])

for a in arr2:
    if len(a) > 1:
        print(a[0], a[1])
    else:
        print(a[0])