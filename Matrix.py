import sys
import os
from conversor import* 
from Definitions import*
SEPARATOR=","
SUFFIX="0x"
BASE_HEX=16
NIBBLE=4
class CMatrix():

	def __init__(self,Line,exit_file):
		self.__Line=Line
		self.__Values=self.__Row_Val()
		self.__I=0
		self.__fd=exit_file
	def __getitem__(self,Args):
		Num_Diag=Args[0]+Args[1]
		idx=Num_Diag;
		Max=len(self.__Line)-1
		if (Num_Diag>Max):
			idx=Num_Diag-Max-1
		return self.__Line[idx]
	def __Row_Val(self):
		Values=[]
		for Row_id in range(len(self.__Line)):
			ret_val=0
			i=0
			for Col in reversed(range(len(self.__Line))):
				ret_val+=decode(self[Row_id,Col],i)
				i+=1
			Values.append(ret_val)
		return Values
	def Get_Values(self):
		return self.__Values
	def Set_Init(self,I):
		self.__I=I
	def __Write_bin_value(self,aux):
		i=0
		bin_buffer=[]
		for elem in aux:
			i+=1
			bin_eq=bin(int(SUFFIX+elem,BASE_HEX))
			bin_eq=bin_eq.lstrip("0b")
			if len(bin_eq)==0:
				bin_eq=elem
			bin_eq=",".join(bin_eq)
			bin_eq=bin_eq.split(",")
			padding_value=NIBBLE-len(bin_eq)
			if padding_value !=0:
				bin_eq=["0"]*padding_value+bin_eq
			bin_buffer+=bin_eq
			if i%2==0:
#				print bin_buffer
				bit_string="0b"+''.join(bin_buffer)
				print bin_buffer
				print "Escribo 1 char ",chr(int(bit_string,2))
				self.__fd.write(chr(int(bit_string,2)))
				bin_buffer=[]
	def Write_Init(self):
		self.__fd.write(",")
		hex_eq=hex(self.__I)
#		print "I= ",self.__I
		aux=hex_eq.lstrip(SUFFIX)
		if len(aux)==0:
			aux=str(self.__I)
		aux=SEPARATOR.join(aux)
		aux=aux.split(SEPARATOR)
		if len(aux)%2!=0:
			aux.insert(0,"0")
		self.__Write_bin_value(aux)
		self.__fd.write("\n")
