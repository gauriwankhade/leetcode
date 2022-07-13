class Solution(object):
    def romanToInt(self, s):
        romanNums = 'IVXLCDM'
        nums = [1, 5, 10, 50, 100, 500, 1000]
        
        last = s[0]
        result = nums[romanNums.find(last)]
        
        for char in s[1: ]:
            if nums[romanNums.find(last)] == nums[romanNums.find(char)]:
                result += nums[romanNums.find(char)]
            elif nums[romanNums.find(last)] > nums[romanNums.find(char)]:
                result += nums[romanNums.find(char)]
            elif nums[romanNums.find(last)] < nums[romanNums.find(char)]:
                result = result +  nums[romanNums.find(char)] - (2 * nums[romanNums.find(last)])
           
                
            last = char
            
        return result
        
            
            