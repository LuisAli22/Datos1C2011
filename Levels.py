import math
from Interval import*
from Definitions import*
ESC=-1
class Levels():
	def __init__(self):
		self.__Emited_Val={}
	def __Get_Default_Value_in_Level(self,Level_id):
		return math.ceil(math.pow(BASE,Level_id-1)) +1
		
	def Is_in_Level(self,Level_id,num):
		init,end=Get_extremeValues(Level_id)
		if (num>=init)and(num<=end):
			return True
		return False
		
	def Probability(self,num,level_id):
		Def_Quantity=self.__Get_Default_Value_in_Level(level_id)
		emited_quantity=0
		if num in self.__Emited_Val.keys():
			emited_quantity=self.__Emited_Val[num]
		Total_Quantity=Def_Quantity+emited_quantity
		print"EVALUANDO NUM: ",num
		print"Cantidad por definicion: ",Def_Quantity
		print" Cantidad de emitidos ",emited_quantity
		return (emited_quantity+1)/Total_Quantity
		
	def Emit_Value(self,Val):
		if Val in self.__Emited_Val.keys():
			self.__Emited_Val[Val]+=1
		else:
			self.__Emited_Val[Val]=1
#		self.__interval.update()
