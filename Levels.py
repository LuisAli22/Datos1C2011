import math
BASE=2
class Levels():
	def Is_in_Level(self,Level_id,num):
		init=math.floor(math.pow(BASE,Level_id-1))
		end=math.pow(BASE,Level_id)-1
		if (num>=init)and(num<=end):
			return True
		return False
		
