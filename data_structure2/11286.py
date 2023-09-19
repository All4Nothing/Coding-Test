import sys
input = sys.stdin.readline

from heapq import heappush, heappop

heap = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heappush(heap, (abs(x),x))
    else:
        print(heappop(heap)[1]) if heap else print(0)