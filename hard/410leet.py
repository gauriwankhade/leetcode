
# class Solution(object):
#     def splitArray(self, nums, m):
#         hashmap = {}
#         numLen = len(nums)
#         interval = int(numLen / m)
#         prevSum = None

#         counter = i = 0
#         while(counter < m ):
#             end =  i + interval
#             if counter + 1  >= m:
#                 end = numLen 

#             hashmap[counter] = [i, end - 1, sum(nums[i: end])]
#             counter += 1
#             i += interval



#         for key in range(len(hashmap) - 1):
#             s1 = hashmap[key][2] + nums[hashmap[key + 1][0]]
#             s2 = hashmap[key + 1][2] + nums[hashmap[key][0]]
#             maxSum = max(hashmap[key][2], hashmap[key + 1][2])

#             if maxSum > max(s1, hashmap[key + 1][2] - hashmap[key + 1][0]):
#                 hashmap[key][1] += 1
#                 hashmap[key + 1][2] -= nums(hashmap[key + 1][0])
#                 hashmap[key + 1][0] += 1
#                 hashmap[key][2] = s1
#             elif maxSum > max(s2, hashmap[key][2] - hashmap[key][1]):
#                 hashmap[key][1] -= 1
#                 hashmap[key + 1][2] = s2
#                 hashmap[key][2] -= nums(hashmap[key + 1][0])
#                 hashmap[key + 1][0] -= 1


#         return hashmap





class Solution:
    def splitArray(self, nums, m) :
        
        def linear(maxLimit):
            summ = 0
            div = 1
            for i in nums:
                summ += i
                if summ > maxLimit:
                    summ = i
                    div += 1
            print('mid-', maxLimit, 'div -', div)
            return div
        
        low,high = max(nums),sum(nums)
        
        while low<=high:
            mid = (low+high)//2
            print("low- ", low, "high- ", high, "mid- ", mid)
            if linear(mid) > m:
                low = mid + 1
            else:
                high = mid - 1
        return low



s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(nums, len(nums))
print(s.splitArray(nums, 3))





























