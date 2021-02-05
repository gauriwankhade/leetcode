class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        Dict = {}
        count = 0
        for i in jewels:
            Dict[i] = True
                  
        for j in  stones:
            try:
                Dict[j]
                count+=1
            except:
                pass
        return count
            