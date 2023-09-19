n, m = map(int, input().split())
arr=[]
cnt=0
for _ in range(n):
    arr.append(input())
for _ in range(m):
    if input() in arr:
        cnt += 1
print(cnt)