"""By understanding this question, we only cares about the changes in the smallest number of A"""
import heapq
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        #use heapq
        heapq.heapify(A)
        for k in range(K):
            smallest_n = heapq.heappop(A)
            heapq.heappush(A, -smallest_n)
        return sum(A)
        """
        #iterate k times
        for k in range(K):
            minimum_n = float("inf")
            index = -1
            for i in range(len(A)):
                if A[i] < minimum_n:
                    #find the minimum number in array A, and its index
                    minimum_n = A[i]
                    index = i
            #changes for the smallest number
            if minimum_n == 0:
                break
            A[index] *= -1
            
        return sum(A)
        """