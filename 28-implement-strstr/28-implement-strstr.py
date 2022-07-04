class Solution(object):
    def strStr(self, haystack, needle):
        length = len(needle)
        
        for i in range(len(haystack) - length + 1):
            if haystack[i: i + length] == needle:
                return i
        return -1