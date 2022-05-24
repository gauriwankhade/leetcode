
class Solution(object):
    def minDistance(self, word1, word2):
        #dp1 = (len(word1) + 1) * [[0] * (len(word2) + 1)]
        dp = [[0 for p in range(len(word2)+1)] for q in range(len(word1)+1)]
        
       
        for a in range(1, len(dp)):
        	dp[a][0] = a

        for b in range(1, len(dp[0])):
        	dp[0][b] = b



        for i in range(1, len(dp)):
        	for j in range(1, len(dp[0])):
        		if word1[i - 1] == word2[j - 1]:
        			dp[i][j] = dp[i - 1][j - 1]
        		else:
        			dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        		
    
        return dp

s = Solution()
word1 = ""
word2 = "abcdeabcdx"
print(s.minDistance(word1, word2))



























