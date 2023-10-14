import sys
input = sys.stdin.readline
from itertools import permutations

def check_plus(n):
    for j in range(1, n//2):
        if j != (n-j) and j in prime_lst and (n-j) in prime_lst:
            return True

def check_mul(n, m): 
    while n % m == 0: # 1
        n = n//m # n = 3
    for i in range(1, n//2): 
        if n%i == 0:
            if n//i in prime_lst and i in prime_lst:
                return True

k, m = map(int, input().split())

MAX = 98765 // 10**(5-k)
check = [0] * (MAX + 1)
prime_lst = set()
for i in range(2, MAX+1):
    if check[i] == 0:
        check[i] = 1
        prime_lst.add(i)
        j = 1
        while i * j <= MAX:
            check[i*j] = 1
            j+=1

per = list(permutations(range(10), k))
perm = []
cnt = 0
for item in per:
    if item[0] == 0:
        continue
    n = int(''.join(list(map(str, item))))
    perm.append(n)

for n in perm:
    if check_mul(n, m):
        if check_plus(n):
            cnt += 1
print(cnt)