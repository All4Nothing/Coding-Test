import heapq

heap = []
n = int(input())
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append((a,b))
time.sort()
heapq.heappush(heap, time[0][1])
for i in range(1,n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])
    else:
        heapq.heappush(heap, time[i][1])
print(len(heap))
