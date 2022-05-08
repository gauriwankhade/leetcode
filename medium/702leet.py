

class ArrayReader(object):
    def __init__(self, nums):
        self.nums = nums
    def get(self, index):
        try:
            return self.nums[index]
        except:
            return None




class Solution(object):
    def search(self, reader, target):
        start = 0
        end = 10**4
        mid = None

        while(start < end):
            mid = int((start + end)/2)
            midVal = reader.get(mid)

            if not midVal:
                end = mid 
            if midVal == target:
                return mid
            if midVal and midVal > target:
                end = mid 
            if midVal and midVal  < target:
                start = mid + 1

        return -1


s = Solution()
nums = [5]
r = ArrayReader(nums)
print(nums)
print(s.search(r, nums))




