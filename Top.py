from Binary import*

class Top(Binary):

	def __init__(self,number):
		Binary.__init__(self,number)
	
	def add_value(self,other):
		for pos in range(self.Get_pos(),other):
			self.append("1")
