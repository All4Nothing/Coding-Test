import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def make_tree(arr):
    if len(arr) == 1:
        return

    root = arr[0]

    idx = 0
    while idx < len(arr):
        if arr[idx] > root:
            break
        idx += 1

    if idx == len(arr): # only l
        l_tree = arr[1:]
        r_tree = [None]
    elif idx == 1: # only r
        l_tree = [None]
        r_tree = arr[idx:]
    else:
        l_tree = arr[1:idx]
        r_tree = arr[idx:]

    tree[root] = [l_tree[0], r_tree[0]]
    make_tree(l_tree)
    make_tree(r_tree)

def preorder_tree(root):
    if root == None:
        return
    if tree.get(root) == None:
        print(root)
        return
    preorder_tree(tree[root][0])
    preorder_tree(tree[root][1])
    print(root)

tree = {}
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
make_tree(arr)

preorder_tree(arr[0])
# preorder_tree(list(tree.keys())[0])