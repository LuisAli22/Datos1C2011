import sys
import os
from conversor import* 
class CMatrix():

	def __init__(self,Line):
		self.__Line=Line
	
	def __getitem__(self,Args):
		Num_Diag=Args[0]+Args[1]
		idx=Num_Diag;
		Max=len(self.__Line)-1
		if (Num_Diag>Max):
			idx=Num_Diag-Max-1
		return self.__Line[idx]

	def Row_Val(self,Row_id):
		ret_val=0
		i=0
		for Col in reversed(range(len(self.__Line))):
			ret_val+=decode(self[Row_id,Col],i)
			i+=1
		return ret_val
	def Size(self):
		return len(self.__Line)
	def Col(self,Col_id):
		return [self[row_id,Col_id] for row_id in range(len(self.__Line))]
