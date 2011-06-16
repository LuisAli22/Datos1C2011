from Interval import*

class Modelo_Estructurado():
	def __init__(self,fichero):
		self.__interval=Interval(fichero)
	def Get_res_number(self):
		return self.__interval.Get_res_number()
	def All_data_stored(self):
		return self.__interval.All_data_stored()
	def Bit_padding(self):
		self.__interval.Bit_padding()
	def run(self,elem):		
		Level_id=0
		while (not self.__interval.Is_in_Level(Level_id,elem)):
			self.__interval.Emit(ESC,Level_id)
			Level_id+=1
		self.__interval.Emit(elem,Level_id)	
