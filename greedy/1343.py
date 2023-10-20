def p(l):
    if l % 2 == 0:
        a = l // 4
        b = l%4 // 2
        return 'AAAA'*a + 'BB'*b
    else:
        return -1

arr = input()
l = 0
ans=[]
for i in arr:
    if i == '.':
        ans.extend([p(l),'.'])
        l = 0
    else:
        l += 1
if l:
    ans.append(p(l))
if -1 in ans:
    print(-1)
else:
    print(*ans, sep='')