from itertools import permutations

def check_prime(n):
    for i in range(2, n+1):
        if n % i == 0:
            break
    if n == i:
        return True
    else:
        False

def check_plus(n):
    for j in range(1, n):
        if check_prime(j) and check_prime(n-j):
            return True

def check_mul(n, m):
    while n // m != 0:
        p = n % m
        n = n//m
    for i in range(1, p+1):
        if p%i == 0:
            if check_prime(p//i) and check_prime(i):
                return True

k, m = map(int, input().split())
num = ['0','1','2','3','4','5','6','7','8','9']
per = list(permutations(num, k))
perm = []
for item in per:
    n = int(''.join(list(map(str, item))))
    perm.append(n)

for n in perm:
    if check_plus(n) and check_mul(n, m):
        print(n)