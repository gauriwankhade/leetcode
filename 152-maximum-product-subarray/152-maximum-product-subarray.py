class Solution(object):
    def maxProduct(self, nums):
		maxx = minn = 1
		maxProduct = max(nums)

		for num in nums:
			if num == 0:
				maxx = minn = 1
				continue

			temp = maxx * num
			maxx = max(num, maxx * num, minn * num)
			minn = min(num, temp, minn * num)

			maxProduct = max(maxProduct, maxx)

		return maxProduct
		
