
class Solution(object):

	def rotate(self, matrix):
		maxIndex = len(matrix) - 1
		n = len(matrix)

		
		for i in range(int(n / 2)  + (n % 2)):
			for j in range(int(n/2)):
				# print('i- ', i, 'j - ', j)
				
				# print(maxIndex - j, i)
				# print(maxIndex - i, maxIndex - j)
				# print(j, maxIndex - i)
				# print(i, j)
			
				temp = matrix[i][j]

				matrix[i][j] = matrix[maxIndex - j][i]
				matrix[maxIndex - j][i] = matrix[maxIndex - i][maxIndex - j]
				matrix[maxIndex - i][maxIndex - j] = matrix[maxIndex - (maxIndex - j)][maxIndex - i]
				matrix[maxIndex - (maxIndex - j)][maxIndex - i]  = temp

				
			

		return matrix

# n - j, i
# n = 3

# [0, 2] -> val(1, 0)
# [1, 0] -> val(3, 1)
# [3, 1] -> val(2, 3)
# [2, 3] -> val(0, 2)

# [0, 1] -> val(2, 0)
# [2, 0] -> val(3, 2)
# [3, 2] -> val(1, 3)
# [1, 3] -> val(0, 1)


# val[0, 0] -> [0, 2] 
# val[0, 2] -> [2, 2] 
# val[2, 2] -> [2, 0]
# val[2, 0] -> [0, 0]

# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

# i, j -> n - j, i
# 0, 0 -> n - j, i

# cycle - 1
# 	i = [0, n - 1]
# 	j = [0, n - 1]

# 	[0, 0] -> [0, 4] -> [4, 4] -> [4, 0] -> [0, 0]

# 	[0, 0] -> [0, 2] -> [2, 2] -> [2, 0] -> [0, 0]


# cycle - 2
# 	i = [0, n - 1]
# 	j = [0, n - 1]

# 	[0, 1] -> [1, 4] -> [4, 3] -> [3, 0] -> [0, 1]

# 	[0, 1] -> [1, 2] -> [2, 1] -> [1, 0] -> [0, 1]

# cycle - 3

# 	[0, 2] -> [2, 4] -> [4, 2] -> [2, 0] -> [0, 2]


# cycle - 4

# 	[0, 3] -> [3, 4] -> [4, 1] -> [1, 0] -> [0, 3]





s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
print(s.rotate(matrix))
