import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr1 = []
    arr2 = []
    input()
    arr1 = set(map(int, input().split()))
    input()
    arr2 = list(map(int, input().split()))
    
    for item in arr2:
        if item in arr1:
            print(1)
        else:
            print(0)