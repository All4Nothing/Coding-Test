m, n = int(input()), int(input())
p = [i for i in range(m, n+1) if all([i%j for j in range(2,i)]) and i > 1]
print(f'{sum(p)}\n{p[0]}' if p else -1)