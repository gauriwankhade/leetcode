class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alpha=string.ascii_lowercase
        Dict = {}
        word = ''
        
        for i in words:
            for j in i:
                ind = alpha.index(j)
                word+= morse[ind]
            Dict[word] = True
            word = ''
            
        return len(Dict)
                