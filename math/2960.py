def find(arr, cnt):
    for i in range(len(arr)):
        if arr[i]:
            p = i+2
            for j in range(len(arr)):
                if arr[j]:
                    if (j+2)%p == 0:
                        cnt += 1
                        if cnt == k:
                            return j+2
                        arr[j] = False
n, k = map(int, input().split())
arr = [True] * (n-1)
print(find(arr, 0))