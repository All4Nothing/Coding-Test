# DFS
sys.setrecursionlimit(10**6) # 재귀 깊이 변경

def DFS(tree, vertex, visited):
    for node in tree[vertex]:
        if not visited[node]:
            visited[node] = vertex
            DFS(tree, node, visited)

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [None for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


DFS(tree, 1, parent)

for i in range(n-1):
    print(parent[i+2])

