import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    cnt = 1
    n, m = map(int, input().split())
    arr = deque(input().split())
    arr2 = deque([0]*n)
    arr2[m] = 1
    while len(arr):
        if max(arr) == arr[0]:
            arr.popleft()
            if (arr2.popleft()) :
                print(cnt)
                break
            else:
                cnt += 1
        else:
            arr.rotate(-1)
            arr2.rotate(-1)