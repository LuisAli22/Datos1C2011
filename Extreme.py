from Buffer import*
from Top import*
from Bottom import*
two_Msb_top=0b10
two_Msb_bottom=0b01
base_one_MSB=0x80;
base_two_MSB=0x40;
first_digit_base=100
class Extreme_Interval():
	def __init__(self,fichero):
		self.__counter=0
		self.__bottom=Bottom(0x00);
		self.__top=Top(0xFF);
		self.__bits=Buffer(fichero)
	def __Is_underflow(self):
		return self.__top[:2]=="10" and self.__bottom[:2]=="01"
#		if self.__top>9 and self.__bottom>9:
#			First_digit_top=self.__top/first_digit_base
#			First_digit_bottom=self.__bottom/first_digit_base
#			print self.__top
#			print self.__bottom
#			print "primer digito top: ",First_digit_top
#			print "primer digito bottom",First_digit_bottom
#			dif_in_one= (First_digit_top-First_digit_bottom)==1
#			if dif_in_one: print "ES VERDAD"
#			top_list=",".join(str(self.__top))
#			top_list=top_list.split(",")
#			Second_digit_top=int(top_list[1])
#			bottom_list=",".join(str(self.__bottom))
#			bottom_list=bottom_list.split(",")
#			Second_digit_bottom=int(bottom_list[1])
#			if len(top_list)==len(bottom_list):
#				return Second_digit_top==0 and Second_digit_bottom==9 and dif_in_one
#		return False
	def __Get_list(self,number):
		string=",".join(str(number))
		return string.split(",")
#	def __Shift_extremes(self):
#		top_list=self.__Get_list(self.__top)
#		bottom_list=self.__Get_list(self.__bottom)
#		del top_list[1]
#		del bottom_list[1]
#		top_list.append("9")
#		bottom_list.append("0")
#		self.__top=int("".join(top_list))
#		self.__bottom=int("".join(bottom_list))
	def __Process_Underflow(self):
		while self.__top.Is_Underflow(self.__bottom):
#			print "UNDERFLOW!!!!!!!"
			self.__counter+=1;
			self.__shift()
	def __shift(self):
		self.__top<<1
		self.__bottom<<1
#		if bit_bot==1:
#			self.__bottom-=0x80
#			self.__top-=0x80
#		self.__bottom*=2
#		self.__top*=2
#		self.__top+=1
	def __Store_Partial_result(self):
#		bit_bot=self.__bottom/base_one_MSB;
#		bit_top=self.__top/base_one_MSB;
		
		while self.__top[0]==self.__bottom[0]:
#			print "bit bot ",bit_bot
#			if bit_bot==0: print "SON CERO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			self.__bits.append(chr(ord("0")+int(self.__top[0])))
			bit_complement=int(bin(~int(self.__top[0]))[-1])
			for i in range(self.__counter):
				self.__bits.append(chr(ord("0")+bit_complement))
			self.__counter=0
#			print "corro 1 lugar"
			self.__shift()
#			print "top: ",int(self.__top)
#			print "bottom: ",int(self.__bottom)

	def Get_length(self):		
		return int(self.__top)-int(self.__bottom)
	def Get_Top(self):
		return int(self.__top)
	def Get_Bottom(self):
		return int(self.__bottom)
	def Set_extremes(self,bottom,top):
		self.__bottom.Set_value(bottom)
		self.__top.Set_value(top)
	def update_bottom(self,value):
#		print "Antes... bottom: ",int(self.__bottom)
#		print value
		self.__bottom+=int(value)
#		print "Despues... bottom: ",int(self.__bottom)
	def update_top(self,my_distance):
#		print "Antes... top: ",int(self.__top)
#		print "Distancia: ",my_distance
#		print "bottom + distancia: =",int(self.__bottom)+int(my_distance)
		self.__top.Set_value(int(self.__bottom)+ int(my_distance))
#		print "Despues... top: ",int(self.__top)
	def normalizate(self):
#		print "top: ",int(self.__top)
#		print "bottom: ",int(self.__bottom)
		self.__Process_Underflow();
		self.__Store_Partial_result();
	def All_data_stored(self):
		return self.__bits.All_data_stored();
	def Bit_padding(self):
		self.__bits.Bit_padding()
