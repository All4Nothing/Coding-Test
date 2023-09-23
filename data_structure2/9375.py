import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = {}
    for _ in range(int(input())):
        v, k = input().split()
        if not clothes.get(k):
            clothes[k] = []
        clothes[k].append(v)

    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1