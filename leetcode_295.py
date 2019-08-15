class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def addNum(self, num: int) -> None:
        low = 0
        high = len(self.stack) - 1
        """Use binary search for insertion"""
        while low <= high:
            middle = (low+high) //2
            if self.stack[middle] >= num:
                high = middle - 1
            else:
                low = middle + 1
        self.stack.insert(low, num)
        

    def findMedian(self) -> float:
        middle = len(self.stack) //2
        if len(self.stack) % 2 == 0:
            
            return (self.stack[middle] + self.stack[middle-1])/2.0
        else:
            return self.stack[middle]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()