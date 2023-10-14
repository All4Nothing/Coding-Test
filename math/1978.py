n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    temp = [j for j in range(1, arr[i]) if arr[i]%j < 1]
    if len(temp) == 1:
        cnt += 1
print(cnt)