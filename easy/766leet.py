class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(1,row):
        	for j in range(1,col):
        		#print(matrix[i][j],matrix[i-1][j-1])
        		if matrix[i][j] != matrix[i-1][j-1]:
        			return False
        return True 
