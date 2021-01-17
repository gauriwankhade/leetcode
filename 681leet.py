class Solution:
	def nextClosestTime(self, time: str) -> str:
		self.convert_str_to_hashmap(time)	
		self.time = time

		raw_time = time.split(':')
		hr = int(raw_time[0])
		m = int(raw_time[1])

		for i in range(24):
			for j in range(60):
				#increment minute
				m+=1
				m = m % 60

				if m== 0: 			#minute cycle complete, increment hour
					break

				time = str(hr) + ':' + str(m)
				if self.check_valid_time(time):
					return self.time

			#increment hour
			hr+=1
			hr = hr % 24
			time = str(hr) + ':' + str(m)

			if self.check_valid_time(time):
				return self.time
		
		return self.time	

	def convert_str_to_hashmap(self,time):
		time = time.replace(':','')  
		self.dict = {}
		for i in time:
			self.dict[int(i)] = True

	def format_time(self,time):
		time = time.split(':')
		hr = time[0]
		m = time[1]

		if int(hr)< 10:
			hr = '0' + hr
		if int(m) < 10:
			m = '0' + m
		time = hr + m
		return time

	def check_valid_time(self,time):	
		time = self.format_time(time)
		for i in time:
			try:
				self.dict[int(i)]
			except:
				return False
		
		self.time = time[0:2] + ':' + time[2:]
		return True
