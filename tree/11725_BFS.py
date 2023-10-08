from collections import deque

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([1])
while q:
    s = q.popleft()
    for v in tree[s]:
        if not parent[v]:
            q.append(v)
            parent[v] = s 

for i in parent[2:]:
    print(i)