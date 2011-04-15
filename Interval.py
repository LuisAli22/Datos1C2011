from Levels import*
from Definitions import*
START_LEVEL =0
POS_MIN=1
class Interval():
	def __init__(self):
		self.__Levels=Levels()
		self.__intermediate_values=[0,1]
		self.__Long=1
	def Get_res_number(self):
		return (self.__intermediate_values[-1] + self.__intermediate_values[0])/2
	def __Get_First_in_Level(self,level_id):
		return math.floor(pow(BASE,level_id-1))
	def __Load_Val(self,level_id):
		res=self.__intermediate_values[0]
		Top=self.__intermediate_values[-1]
		self.__Long=Top-res
		self.__intermediate_values=self.__intermediate_values[:1]
		num=self.__Get_First_in_Level(level_id)
		count=1
		Max_Quantity=self.__Levels.Get_Default_Value_in_Level(level_id)
		while (res < Top):
			prob=self.__Levels.Probability(num,level_id)
#			print"num: ",num,"\tprob: ",prob,"\tL: ",self.__Long
			res+=(prob*(self.__Long)) 	
			self.__intermediate_values.append(res)	
			num+=1
			count+=1
			if count==Max_Quantity:
				num=ESC

	def __Get_new_extreme(self,Val,level_id):
		Idx=int(Val- self.__Get_First_in_Level(level_id))
		return Idx,Idx+2
	def __Update_Interval_extreme(self,Val,Level_id):
		if (Val==ESC):
			self.__intermediate_values=self.__intermediate_values[-2:]
		else:
			if Val==self.__Get_First_in_Level(Level_id):
				self.__intermediate_values=self.__intermediate_values[:2]
			else:
				bottom,Top=self.__Get_new_extreme(Val,Level_id)
				self.__intermediate_values=self.__intermediate_values[bottom:Top]
		
	def Emit_Value(self,Val,Level_id):	
		self.__Load_Val(Level_id)
#		print "I: ",self.__intermediate_values
		self.__Update_Interval_extreme(Val,Level_id)
		self.__Levels.Emit_Value(Val)
	def Is_in_Level(self,Level_id,num):
		return self.__Levels.Is_in_Level(Level_id,num)

		
