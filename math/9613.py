from itertools import combinations

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

for _ in range(int(input())):
    ans = 0
    arr = list(map(int, input().split()))
    com = list(combinations(arr[1:], 2))
    for item in com:
        a, b = item
        ans += gcd(a, b)
    print(ans)
