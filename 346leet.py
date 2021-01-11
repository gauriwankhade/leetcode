# ******* unoptimised Approach  ***********

# class MovingAverage:

#     def __init__(self, size: int):
#         self.size = size
#         self.queue = []
        

#     def next(self, val: int) -> float:
#         l = len(self.queue)
#         if l >= self.size:
#             self.queue.pop(0)
#             l-=1
        
#         self.queue.append(val) 
#         l+=1
#         ans = sum(self.queue)/float(l)
#         



# ********  Approach 2 *************

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.arr = []
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum+= val
        self.arr.append(val)

        if len(self.arr) > self.size:
            self.sum-= self.arr.pop(0)
        return self.sum/float(len(self.arr))


