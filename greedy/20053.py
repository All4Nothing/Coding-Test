import sys
input = sys.stdin.readline

#QuickSort
def sort(arr):
    if len(arr) == 1:
        return arr
    left, right, mid = []
    pivot = arr[len(arr)//2]
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)
    return sort(left) + mid + sort(right)
        

for _ in range(int(input())):
    int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0], arr[-1])