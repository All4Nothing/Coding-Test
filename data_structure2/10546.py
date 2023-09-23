db = {}
import sys
input = sys.stdin.readline
for _ in range(n:=int(input())):
    p = input()
    if not db.get(p):
        db[p] = 0
    db[p] += 1

for _ in range(n-1):
    p = input()
    db[p] -= 1

for key, value in db.items():
    if value > 0:
        print(key)