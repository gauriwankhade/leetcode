

class Solution(object):
    def findTheWinner(self, n, k):
        Arr = list(range(1, n + 1))
        length = len(Arr)
        ref = 0
        ans = 0

        while Arr:
        	rem = (ref + k - 1) % length
        	ans = Arr.pop(rem)
        	ref = rem
        	length -= 1
        

        return ans



s = Solution()
print(s.findTheWinner(5, 2))
