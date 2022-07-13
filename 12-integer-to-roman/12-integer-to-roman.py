class Solution(object):
    def intToRoman(self, num):
        # Map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        romanNums = ['I','IV', 'V', 'IX', 'X', 'XL','L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        nums      = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
#         romanNums = romanNums[::-1]
#         nums = nums[::-1]
        
        ans = ''
        counter = 12
        while(num > 0):
            #print(num)
            if nums[counter] <= num:
                num -= nums[counter]
                ans += romanNums[counter]
            else:
                counter -= 1

        return ans
                