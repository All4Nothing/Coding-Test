k = int(input())
arr = list(map(int, input().split()))

tree = [None for i in range(2**k-1)]

def make_tree(arr, idx):
    if idx >= 2**k - 1: #
        return 
    mid = len(arr) // 2 
    tree[idx] = arr[mid]
    make_tree(arr[:mid], idx*2 + 1)
    make_tree(arr[mid+1:], idx*2 + 2)

make_tree(arr, 0)

l = 0
while l < 2**k:
    print(*tree[l:l*2+1])
    l = l*2 + 1