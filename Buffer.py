N_BIT=8
class Buffer():
	
	def __init__(self,fichero):
		self.__fd=fichero;
		self.__bits=[]
	def __write(self):
		bit_string="0b"+''.join(self.__bits)
		print self.__bits
		print self.__bits
		print "Escribo 1 char ",chr(int(bit_string,2))
		self.__fd.write(chr(int(bit_string,2)))
		self.__bits=[]

	def All_data_stored(self):
		if len(self.__bits)==0:
			return True
		return False
	def Bit_padding(self):
		padding_amount=N_BIT - len(self.__bits)
		self.__bits=self.__bits + ["0"]*padding_amount
		self.__write()
	def append(self,obj):
		self.__bits.append(obj)
		if len(self.__bits)==N_BIT:
			self.__write()
