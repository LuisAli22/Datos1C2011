from Levels import*
from Definitions import*
START_LEVEL =0
POS_MIN=1
class Interval():
	def __init__(self):
		self.__Levels=Levels()
		self.__lower_value=0
		self.__upper_value=1
		self.__Long=self.__upper_value - self.__lower_value
		self.__intermediate_values=[]
		self.__Load_Val(START_LEVEL,START_LEVEL)
		print self.__intermediate_values
	def __Load_Val(self,num,level_id):
		res=self.__lower_value
		self.__intermediate_values.append(res)
		prob=self.__Levels.Probability(num,level_id)
		print "Nivel ",level_id," Prob: ",prob
		while (res < self.__upper_value):
			res+=(self.__lower_value+prob*(self.__Long)) 	
			self.__intermediate_values.append(res)	
		print self.__intermediate_values
		
	def __new_limits(self,begin,end,offset,My_length_offset):
		begin=begin+offset
		end=begin+My_length_offset
	def __update_only_one(self,Edge,My_length_offset):
		Edge=Edge+My_length_offset
	def __Get_Probabilites(self,Val,level_id,distance):	
		
	def __update_both(self,Val,level_id,distance,from_upper,My_length_offset):
		offset=self.__Get_Probabilites(Val,level_id,distance)*self.__Long
		if from_upper:
			self.__new_limits(self.__upper_value,self.__lower_value,-offset,-My_length_offset)
		else:
			self.__new_limits(self.__lower_value,self.__upper_value,offset,My_length_offset)

	def __Set_New_Interval(self,Val,level_id,from_upper,distance):
		My_length_offset=self.__Levels.Probability(Val,level_id)*self.__Long
		if (distance==0 ):
			if Val==ESC:
				self.__update_only_one(self.__lower_value,-My_length_offset)
			else:
				self.__update_only_one(self.__upper_value,My_length_offset)
		else:
				self.__update_both(Val,level_id,distance,from_upper,My_length_offset)
			
	def __Update_Interval(self,Val,Level_id):
		lower,upper=Get_extremeValues(Level_id)
		Distance=[[0,Val-lower],[1,upper-Val]]
#		print Distance
		from_upper=False
		minor=find_min(Distance,from_upper)
		self.__Set_New_Interval(Val,Level_id,from_upper,minor[POS_MIN])
		
	def Emit_Value(self,Val,Level_id):
		self.__Levels.Emit_Value(Val)
		self.__Update_Interval(Val,Level_id)
	def Is_in_Level(self,Level_id,num):
		return self.__Levels.Is_in_Level(Level_id,num)
	def run(self,num):
		Level=self.__Levels.Get_Level(num)
		self.__Load_Val(num,Level)

		
