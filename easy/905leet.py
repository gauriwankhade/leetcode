class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        start = 0
        end = len(A)-1

        while(start<end):
            if A[start]%2 > A[end]%2:
                A[start],A[end] = A[end],A[start]
        
            if A[start]%2 == 0:
                start+=1
            if A[end]%2 == 1:
                end-= 1

        return A


s = Solution()
A = [0,1,2]
print(s.sortArrayByParity(A))