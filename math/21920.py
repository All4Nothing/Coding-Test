'''
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
'''
from math import gcd

n = input()
arr = list(map(int, input().split()))
x = int(input())
l = []
for i in arr:
    if gcd(x, i) == 1:
        l.append(i)
print(sum(l)/len(l))
