class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        count = 0
        for i in range(len(word)-1):
             count+= abs(keyboard.index(word[i+1])-keyboard.index(word[i]))
                   
        count+=keyboard.index(word[0])
        
        return count
            
        
            
        