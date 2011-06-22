import math
from abc import ABCMeta,abstractmethod
from Definitions import*
N_BITS=8
class Binary():
	__metaclass__=ABCMeta
	def __init__(self,value):
#		self.__number=value
		self.__bin=self.__get_bin(value)
		self.__pos=0
	def Set_pos(self,n_pos):
		self.__pos=n_pos
	def Get_pos(self):
		return self.__pos
	def __getitem__(self,index):
		return self.__bin[index]
	def __setitem__(self, key, value):
	    self.__bin.__setitem__(self, key, value)

	def __delitem__(self, key):
	    self.__bin.__delitem__(self, key)
	def __iadd__(self,value):
		number=int("".join(self.__bin),BASE)
		number+=value
		self.__bin=self.__get_bin(number);
		return self
	def __isub__(self, value):
		number=int("".join(self.__bin),BASE)
		number-=value
		self.__bin=self.__get_bin(number);
		return self
	def __imul_(self,value):
		number=int("".join(self.__bin),BASE)
		number *=value
		self.__bin=self.__get_bin(number);
		return self
	def __sub__(self, value):
		return int("".join(self.__bin),BASE) - value.get_numeric_value()
	def __int__(self):
		return int("".join(self.__bin),BASE)
	def __lshift__(self,other):
		for pos in range(self.__pos,other):
			del self.__bin[pos]
#		self.__bin.append("1")
#		print "El numero queda: ",int(self)
		self.add_value(other)
#		print "Leugo de sumarle lo que corresponda, queda: ",int(self)
		self.__pos=0
#		self.__number=int("".join(self.bin),2)
#		num=int(self.__number)<<other
#		self.__number += num-math.pow(2,N_BITS);
#		self.__bin=self.__get_bin();
	def __repr__(self):
		return self.__bin;
	def __eq__(self,value):
		return int("".join(self.__bin),BASE)==value;  
	def __get_bin(self,number):
		my_bin=bin(int(number)).lstrip("0b");
		num=N_BITS-len(my_bin)
		if num >0:
		    cadena="0"*num;
		    my_bin=cadena+my_bin;
		aux_bin=",".join(my_bin)		 
		return aux_bin.split(",")
	def Set_value(self,value):
		self.__bin=self.__get_bin(value)
	def append(self,value):
		self.__bin.append(value)
#	def get_numeric_value(self):
#		return int(self.__bin)
#	def Get_bin_value(self):
#		return self.__bin
	@abstractmethod
	def add_value(self,other):
		pass
#	def Shift_Top(self):
#		del self.__bin[1]
#		self.__bin.append("1")
#		self.add_value()
#		self.__number=int("".join(self.bin),2)
	def Is_Underflow(self,Bottom):
		if self[:2]=="10" and Bottom[:2]=="01":
			self.Set_pos(1)
			Bottom.Set_pos(1)
			return True
		return False
		
