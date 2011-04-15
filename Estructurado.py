from Interval import*

class Modelo_Estructurado():
	def __init__(self):
		self.__interval=Interval()
		
	def __Search_and_find_Level(self,num,fichero):
		Level_id=0
		while (not self.__interval.Is_in_Level(Level_id,num)):
			self.__interval.Emit_Value(ESC,Level_id,fichero)
			Level_id+=1
		self.__interval.Emit_Value(num,Level_id,fichero)	
	def Get_res_number(self):
		return self.__interval.Get_res_number()
	def run(self,elem,fichero):		
		self.__Search_and_find_Level(elem,fichero)
