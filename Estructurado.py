from Interval import*

class Modelo_Estructurado():
	def __init__(self):
		self.__interval=Interval()
		
	def __Search_and_find_Level(self,num):
		Level_id=0
		while (not self.__interval.Is_in_Level(Level_id,num)):
			self.__interval.Emit_Value(ESC,Level_id)
			Level_id+=1
		self.__interval.Emit_Value(num,Level_id)	
	
	def run(self,Entry_list):
		for elem in Entry_list:
			print elem		
			self.__Search_and_find_Level(elem)
#			print elem," en nivel ",self.__Levels.Get_Level(elem)	
