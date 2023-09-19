import heapq
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    max_heap,min_heap = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(max_heap, (int(num), j))
            heapq.heappush(min_heap, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        a = -min_heap[0][0]
        b = max_heap[0][0]
        print("%d %d" % (a, b))