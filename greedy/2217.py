lope=[]
ans = []
for _ in range(n:=int(input())):
    lope.append(int(input()))
lope.sort()
for i in lope:
    ans.append(i*n)
    n -= 1
print(max(ans))