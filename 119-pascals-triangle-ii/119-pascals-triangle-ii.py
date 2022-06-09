class Solution(object):
	def getRow(self, rowIndex):
		ans = [1]

		for i in range(1, rowIndex + 1):
			newArr = ans + []
			for j in range(1, i):
				newArr[j] = newArr[j] + ans[j - 1]

			newArr.append(1)
			ans = newArr


		return ans
