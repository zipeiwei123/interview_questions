"""Sort the list in a priorityQueue/ Minheap, then check adjancent time slot to see if it collide"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #special case
        if not intervals:
            return  0 
        #sort the interval according to start time
        sorted_interval = sorted(intervals, key = lambda x: x[0])
        #use a heap to check the time
        heap = []
        for i in sorted_interval:
            #if the start time exist and you don't need to allocate room
            if heap and i[0] >= heap[0]:
                #update the end time 
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        
        return len(heap)
     
    
        