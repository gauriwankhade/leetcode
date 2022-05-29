from collections import defaultdict

class Solution(object):
    def permute(self, nums):
        graph = defaultdict(list)
        result = []
        numLen = len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                                    
                graph[nums[i]].append(nums[j])

        
        def recursion(num, curr, visited):
            for i in graph[num]:
                if not visited.get(i):
                    visited[i] = True
                    recursion(i, curr + [i], visited)

            visited[num] = False
            if len(curr) == numLen:
                result.append(curr)


        for num in nums:
            visited = {num: True}
            recursion(num, [num], visited)
            
            
        return result
            