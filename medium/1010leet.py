from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time):
        hashmap = defaultdict(int)
        for t in time:
            hashmap[t%60] += 1

        result = 0
        for i in hashmap:
            if i == 0 or i == 30:
                result+= int(hashmap[i] * (hashmap[i] - 1) / 2)
            elif i < 30 and 60 - i in hashmap:
                result+= (hashmap[60 - i] * hashmap[i])


        return result


s = Solution()
print(s.numPairsDivisibleBy60([60, 60, 60]))







