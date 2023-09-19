import sys
input = sys.stdin.readline

import heapq
heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x,x))
    else:
        print(heapq.heappop(heap)[1]) if heap else print(0)