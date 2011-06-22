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
		self.__range=len(self.__Line)
#		self.__Values=self.__Row_Val()
		self.__num_block_repeated=0
		self.__repeated_row=[]
		self.__I=0
		self.__col=0
		self.__fd=exit_file
	def __getitem__(self,Args):
		Num_Diag=Args[0]+Args[1]
		idx=Num_Diag;
		Max=len(self.__Line)-1
		if (Num_Diag>Max):
			idx=Num_Diag-Max-1
		return self.__Line[idx]
	def All_equal(self,First_Time):
		if First_Time:
			return len(set((",".join(self.__Line)).split(",")))==1
		else:	
			aux_list=[]
#			print "repeated row: ",self.__repeated_row
#			print "idx: ",self.__num_block_repeated
			for row_id in self.__repeated_row[self.__num_block_repeated]:
#				print "row_id: ",row_id," col: ",self.__col
				aux_list.append(self[row_id,self.__col]) 
#			print aux_list
			return len(set(aux_list))==1
#		print "All equal: ",self.__repeated_row[self.__num_block_repeated]
#		print "num block repeated: ",self.__num_block_repeated
		if len(self.__repeated_row)>0:
#			print "All equal: ",self.__repeated_row[self.__num_block_repeated]
			return len(set(self.__repeated_row[self.__num_block_repeated]))==1
		return False
	def Out_Of_Range(self):
		return self.__col>=self.__range-1
	
#	def __Row_Val(self):
#		Values=[]
#		for Row_id in range(len(self.__Line)):
#			ret_val=0
#			i=0
#			for Col in reversed(range(len(self.__Line))):
#				ret_val+=decode(self[Row_id,Col],i)
#				i+=1
#			Values.append(ret_val)
#		return Values
	def There_Are_No_Repeated_Rows(self):
		return len(self.__repeated_row)==0
	def Set_Repeated_Rows(self,repeated):
		self.__repeated_row[:]=repeated
#		self.__col+=1
	def Get_Repeated_Rows(self):
		return self.__repeated_row
	def Get_Repeated_Rows_Actual_Elem(self):
		return self.__repeated_row[self.__num_block_repeated]
	def Set_Col(self,col_id):
		self.__col=col_id
	def Inc_Col(self):
		self.__col+=1
	def Dec_Col(self):
		self.__col-=1	
	def Get_Quantity_Repeated_Rows(self):
		return len(self.__repeated_row)
	def Get_Num_Block_Repeated(self):
		return self.__num_block_repeated
	def Set_Num_Block_Repeated(self,block_id):
		self.__num_block_repeated=block_id
	def There_Are_Repeated_Rows(self):
		return len(self.__repeated_row)>0
	def Get_Range(self):
		return self.__range
	def Get_Actual_col(self):
		return self.__col
#	def Get_Values(self):
#		return self.__Values
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
#				print bin_buffer
#				print "Escribo 1 char ",chr(int(bit_string,2))
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
