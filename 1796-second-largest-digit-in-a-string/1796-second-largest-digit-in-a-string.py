class Solution(object):
    def secondHighest(self, s):
        
        firstMax, secondMax = float('-inf'), -1
        
        for char in s:
            if char.isnumeric():
                if firstMax < int(char):
                    firstMax, secondMax = int(char), firstMax
                elif firstMax != int(char):
                    secondMax = max(secondMax, int(char))
        
        return secondMax if secondMax not in [float('-inf'), firstMax] else -1