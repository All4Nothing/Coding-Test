def del_tree(arr):
    for i in arr:
        del_tree(tree[i])
        tree[i] = [-1]
        
n = int(input())

tree = [[] for _ in range(n)]

l = list(map(int, input().split()))
for idx, nd in enumerate(l):
    if nd == -1:
        continue
    tree[nd].append(idx)
    
del_tree([int(input())])

print(tree.count([]))
