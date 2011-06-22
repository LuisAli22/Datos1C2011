import math
from Levels import*
from Definitions import*
from Extreme import*

START_LEVEL =0
POS_MIN=1
class Interval():
	def __init__(self,fichero):
		self.__Levels=Levels()
		self.__extremes=Extreme_Interval(fichero)
		self.__total=0
	def All_data_stored(self):
		return self.__extremes.All_data_stored();
	def Bit_padding(self):
		self.__extremes.Bit_padding();

	def __Get_new_extreme(self,Val,level_id):
		Idx=int(Val- self.__Get_First_in_Level(level_id))
		return Idx,Idx+2
	def __Get_distance(self,total_val,length):
		real_distance=length*(total_val/self.__total);
#		print "Total_val: ",total_val
#		print "total: ",self.__total
#		print "real_distance: ",real_distance
		if math.modf(real_distance)[0]< 0.5 :
		    return math.floor(real_distance)
		return math.ceil(real_distance)

	def __seek_val_in_appropiate_precision(self,length,Level_id,val):
		total_default= self.__Levels.Get_Default_Value_in_Level(Level_id);
		emited_quantity=self.__Levels.Get_emited_in_this_Level(Level_id);
		init=int(self.__Levels.Get_First_in_Level(Level_id))
		self.__total=total_default + emited_quantity;
		total_val=0;
		Last=val;
		if val==ESC:
			Last=self.__Levels.Get_Last_in_Level(Level_id);
		for i in range(init,Last+1):
			total_val+=self.__Levels.Get_emited(i)+1;
		return self.__Get_distance(total_val,length)

	def Emit(self,Val,Level_id):	
		length=self.__extremes.Get_length()
#		print "length: ",length
		self.__total=0
		if self.__extremes.Get_Top() == 0xff:
			length+=1;
		distance=self.__seek_val_in_appropiate_precision(length,Level_id,Val);
		if Val != self.__Levels.Get_First_in_Level(Level_id):
			self.__extremes.update_bottom(distance)
		if Val != ESC:
#			print "Encuentro ",Val," en nivel ",Level_id
			total_val=self.__Levels.Get_emited(Val)+1
#			print "Hay ",total_val," valores ",Val," en nivel ",Level_id
#			print "Hay ",self.__Levels.Get_emited(ESC)," valores ESC en nivel ",Level_id
			distance=self.__Get_distance(total_val,length)
			self.__extremes.update_top(distance)
		self.__extremes.normalizate()
		self.__Levels.Emit_Value(Val)
#		if Val != ESC:
#			print "Encuentro ",Val," en nivel: ",Level_id
            
	def Is_in_Level(self,Level_id,num):
		return self.__Levels.Is_in_Level(Level_id,num)
