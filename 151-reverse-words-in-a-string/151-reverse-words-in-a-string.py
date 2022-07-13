class Solution(object):
    def reverseWords(self, s):
        item = ""
        result = ""
        
        for index in range(len(s)):
            if s[index] != " ":
                item += s[index]
                
            if (s[index] == " " and item):
                result = item + " " + result
                item = ""

        if item and result:     
            return item + " " + result[:len(result) - 1]
        if item and not result:
            return item
        
        return result[:len(result) -1 ]