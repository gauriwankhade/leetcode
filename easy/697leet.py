
#approach 1: single loop
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        count = 1
        sub_len = 0
        
        for ind in range(len(nums)) :
            if num_map.get(nums[ind]) :
                num_map[nums[ind]][1] = ind
                num_map[nums[ind]][2] = num_map[nums[ind]][2] + 1
            else :
                num_map[nums[ind]] = [ind, ind, 1]
            if  num_map[nums[ind]][2] > count 
                    or (num_map[nums[ind]][2] >= count 
                    and num_map[nums[ind]][1] - num_map[nums[ind]][0] <= sub_len) :
                count = num_map[nums[ind]][2] 
                sub_len = num_map[nums[ind]][1] - num_map[nums[ind]][0] + 1
     
        return sub_len



# #approach 2: two loops 
# class Solution(object):
#     def findShortestSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         num_map = {}
#         count = None
#         sub_len = 0
        
#         for ind in range(len(nums)) :
#             if num_map.get(nums[ind]) :
#                 num_map[nums[ind]][1] = ind
#                 num_map[nums[ind]][2] = num_map[nums[ind]][2] + 1
#             else :
#                 num_map[nums[ind]] = [ind, ind, 1]
          
#         for item in num_map:
#             if not count or (count < num_map[item][2]) 
#                 or (count <= num_map[item][2] 
#                 and (sub_len >= num_map[item][1] - num_map[item][0])):
#                 count = num_map[item][2]
#                 sub_len = num_map[item][1] - num_map[item][0] 
            
#         return sub_len + 1

