l = input()
m = l.split('-')
ans = 0

if l[0] == '-':
    ans -= sum(map(int, m[1].split('+')))
    m = m[1:]
else:
    ans += sum(map(int, m[0].split('+')))

for x in m[1:]:
    ans -= sum(map(int, x.split('+')))
print(ans)