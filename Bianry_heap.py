import heapq
heap=[]
(heapq.heappush(heap,1))
heapq.heappush(heap,5)
heapq.heappush(heap,10)
heapq.heappush(heap,17)
heapq.heappush(heap,18)
heapq.heappushpop(heap,89)
print(heapq.nsmallest(2,heap))
print(heapq.nlargest(2,heap))
print(heap)
#hepify function(minheap by default)

