import sys
input = sys.stdin.readline

d = {}

while True:
    tree = input()
    if tree:
        if tree in d:
            d[tree] += 1
        else:
            d[tree] = 1
    else:
        break

s_dict = dict(sorted(d.items()))
n = sum(s_dict.values())
for item in s_dict:
    print(item, round(s_dict[item]/n*100,4))
d = {}

while True:
    tree = input().rstrip()
    if tree:
        if tree in d:
            d[tree] += 1
        else:
            d[tree] = 1
    else:
        break

s_dict = dict(sorted(d.items()))
n = sum(s_dict.values())
for item in s_dict:
    print(item, f'{s_dict[item]/n*100:.4f}')
