n = int(input())

v = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        print("no") if len(v[k]) == 1 else print("yes")
    else:
        print("yes")