class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        ans = 0
        coins = -2
        l = len(piles)
        m = l/3

        while(abs(coins)<=(l-m)):
            ans+= piles[coins]
            coins-= 2
            
        return ans
            
            
s = Solution()
arr = [4,4,17,7,16,16,16,15,2,3,1,17,6,12,9]
print(s.maxCoins(arr))     