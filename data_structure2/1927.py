import sys
input = sys.stdin.readline

from heapq import heappush, heappop

heap = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(heappop(heap)) if heap else print(0)
    else:
        heappush(heap, n)