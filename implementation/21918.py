n, m = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(m):
    c, i, x = map(int, input().split())
    match c:
        case 1:
            if x == 1:
                l[i-1] = True
            else:
                l[i-1] = False
               
        case 2:
            for i in range(i-1, x):
                l[i] = not l[i]
                
        case 3:
            for i in range(i-1, x):
                l[i] = False
        case 4:
            for i in range(i-1, x):
                l[i] = True
                
for i in l:
    print(1, end=" ") if i else print(0, end=" ")         