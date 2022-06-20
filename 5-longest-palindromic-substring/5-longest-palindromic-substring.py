class Solution(object):
     def longestPalindrome(self, s):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        limit = len(dp)
        for row in range(limit):
            dp[row][row] = 1
            if row < limit - 1 and s[row] == s[row + 1]:
                dp[row][row + 1] = 1


        for p in range(2, limit):
            start = 0
            while(start + p < limit):
                if s[start] == s[start + p] and dp[start + 1][start + p - 1] == 1:
                    dp[start][start + p] = 1
                start += 1 

        
        ans = s[0]
        ansLen = 1
        for res in dp:
            start = end = -1
            try:
                start = res.index(1)
                end = limit - 1 - res[::-1].index(1)
                if ansLen <= end - start + 1:
                    ansLen = end - start + 1
                    ans = s[start: end + 1]
            except:
                pass
           


        return ans