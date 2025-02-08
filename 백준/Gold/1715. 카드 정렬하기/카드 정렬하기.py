import sys
import heapq
input = sys.stdin.readline
n = int(input().rstrip())
heap = []
for _ in range(n):
    heapq.heappush(heap,int(input().rstrip()))
count = 0
while len(heap) > 1:
    first_num = heapq.heappop(heap)
    second_num = heapq.heappop(heap)
    plus = first_num + second_num
    count += plus
    heapq.heappush(heap, plus)
print(count)