loc = {}
cnt = 0

for _ in range(int(input())):
    n, l = map(int, input().split())
    x = loc.get(n)
    if x == None:
        loc[n] = l
    else:
        if l != x:
            loc[n] = l
            cnt += 1          
print(cnt)          