
class Solution:
	def __init__(self):
		self.result = 0
		self.binary =''
	def rangeBitwiseAnd(self, m, n):
		if m==0 or n<=0:
			return 0

		self.bitwise_and(m,n)
		return self.result

	def dec_to_binary(self,num,binary=''):
		if num>=1:
			self.dec_to_binary(num//2)
			self.binary+= str(num%2)

		return self.binary
	
	def bitwise_and(self,a,b):
		if a<=0 or b<=0:
			return
		self.binary = ''
		binary_a = self.dec_to_binary(a)
		self.binary = ''
		binary_b = self.dec_to_binary(b)
 		print('binary_a',binary_a,'binary_b',binary_b)
 		if len(binary_a)==len(binary_b):
 			length = len(binary_a)
 			ans = int(2**(length-1))
 			a-= ans
 			b-= ans
 			self.result +=ans
 			self.bitwise_and(a,b) 
 		return
 			

	
s=Solution()
print s.rangeBitwiseAnd(input(),input())