s = input()
t = input()
counter = 0
i = 1

def removeChar(string,counter,i,prev=0):
	limit = len(string)
	while(counter<limit-1 and len(string)>i>1):
		if string[i]=='#':
			try:
				string = string[0:i-1] + string[i+1:]
			except:
				string = string[0:i-1] 
			i-=1
		else:
			i+=1
		counter+=1
		
	print(string)

			
removeChar(s,counter,i)
removeChar(t,counter,i)

