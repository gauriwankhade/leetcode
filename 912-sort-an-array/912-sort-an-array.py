class Solution(object):
    def sortArray(self, nums):
        mergedArr = []
        def merge(arr1, arr2):
            first = second = 0
            currMin = None
            mergedArr = []
            
            while(True):
                if first >= len(arr1):
                    mergedArr.extend(arr2[second: ])
                    break
                if second >= len(arr2):
                    mergedArr.extend(arr1[first: ])
                    break
                if arr1[first] >= arr2[second]:
                    currMin = arr2[second]
                    second += 1
                elif arr1[first] < arr2[second]:
                    currMin = arr1[first]
                    first += 1
                mergedArr.append(currMin)
        
            return mergedArr
            
        
        def mergeSort(left, right):
            if left < right:
                mid = int((left + right) / 2)
                mergeSort(left, mid)
                mergeSort(mid + 1, right)
                sortedArr = merge(nums[left:mid + 1], nums[mid + 1: right + 1])
                nums[left: right + 1] = sortedArr
                
            return nums
 
        return mergeSort(0, len(nums) - 1)
                
            
        
        