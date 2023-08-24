from collections import deque

n, m = map(int, input().split())
o = list(map(int, input().split()))
arr = deque([i for i in range(1, n+1)])
cnt = 0
for i in range(m):
    if arr[0] == o[i]:
        arr.popleft()
        continue
    n = arr.index(o[i])
    if n > len(arr)/2:
        arr.rotate(len(arr)-n)
        cnt += len(arr)-n
    else:
        arr.rotate(-n)
        cnt += n
    arr.popleft()
print(cnt)