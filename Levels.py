import math
from Interval import*
from Definitions import*
ESC=-1
class Levels():
	def __init__(self):
		self.__Emited_Val={}
	def Get_Default_Value_in_Level(self,Level_id):
		return math.ceil(math.pow(BASE,Level_id-1)) +1
	def Get_First_in_Level(self,level_id):
		return math.floor(pow(BASE,level_id-1))
	def Get_Last_in_Level(self,level_id):
		return pow(BASE,level_id)-1
	def Is_in_Level(self,Level_id,num):
		init,end=Get_extremeValues(Level_id)
		if (num>=init)and(num<=end):
			return True
		return False
	def Get_emited_in_this_Level(self,Level_id):	
		emited=0
		for key in self.__Emited_Val.keys():
			if self.Is_in_Level(Level_id,key)or (key==ESC):
				emited+=self.__Emited_Val[key]
		return emited
	def Get_emited(self,val):
		if val in self.__Emited_Val:
		    return self.__Emited_Val[val]
		return 0
#    def Get_Total_Quantity(self,level_id):
#		def_Quantity=self.Get_Default_Value_in_Level(level_id)
#		emited_quantity=self.__Get_emited_in_this_Level(level_id)
#        return def_Quantity + emited_quantity

	def Probability(self,num,level_id):
		Def_Quantity=self.Get_Default_Value_in_Level(level_id)
		emited_quantity=self.__Get_emited_in_this_Level(level_id)
		My_Quantity=1
		if num in self.__Emited_Val.keys():
			My_Quantity+=self.__Emited_Val[num]
		Total_Quantity=Def_Quantity+emited_quantity
		Probability=My_Quantity/Total_Quantity
		return My_Quantity/Total_Quantity
		
	def Emit_Value(self,Val):
		if Val in self.__Emited_Val.keys():
			self.__Emited_Val[Val]+=1
		else:
			self.__Emited_Val[Val]=1
#		if Val==ESC: print "Emito ESC"
#		else:
#			print "Emito ",Val
	def Get_bottom_from_bottom_level(self,Val,Level_id,bottom):
		init=Get_First_in_Level(Level_id)
		Def_Quantity=self.Get_Default_Value_in_Level(Level_id)
		emited_quantity=self.__Get_emited_in_this_Level(Level_id)
		Total=Def_Quantity + emited_quantity;
		counter=0;
		for i in range(init,Val):
			if i in self.__Emited_Val.key():
				counter+=self.__Emited_Val[i];
			else:
				counter+=1;
		
