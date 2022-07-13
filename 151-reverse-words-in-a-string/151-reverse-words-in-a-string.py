class Solution(object):
    def reverseWords(self, s):
        item = ""
        result = ""
        s = s + " "
        
        for index in range(len(s)):
            if s[index] != " ":
                item += s[index]
                
            if (s[index] == " " and item):
                result = item + " " + result
                item = ""

        return result[: len(result) - 1]