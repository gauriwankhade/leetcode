


class Solution(object):
    def findBuildings(self, heights):
        hLen = len(heights)
        counter = hLen - 1
        result = []

        end = 0
        for height in heights[::-1]:
        	if height > end:
        		result = [counter] + result
        		end = height

        	counter -= 1

        return result



s = Solution()
heights = [5, 5, 8]
print(s.findBuildings(heights))



        