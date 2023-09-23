import sys
input = sys.stdin.readline

db = {}
for _ in range(int(input())):
    name = input()
    if not db.get(name):
        db[name] = 0
    db[name] += 1
db2 = dict(sorted(db.items(), reverse = True))
print(sorted(db2.items(), key = lambda x:x[1])[-1][0])