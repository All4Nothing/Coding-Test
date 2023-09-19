import sys
input = sys.stdin.readline

import heapq
heap = []

for _ in range(n:=int(input())):
    arr = list(map(int, input().split()))
    for i in arr:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappush(heap, i)
                heapq.heappop(heap)
print(heap[0])