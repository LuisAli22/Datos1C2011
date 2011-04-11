import sys
import os
from conversor import* 
from Definitions import*
class CMatrix():

	def __init__(self,Line):
		self.__Line=Line
		self.__Permutation_Array=range(len(Line))
		self.__Values=self.__Row_Val()
	def __getitem__(self,Args):
		Num_Diag=Args[0]+Args[1]
		idx=Num_Diag;
		Max=len(self.__Line)-1
		if (Num_Diag>Max):
			idx=Num_Diag-Max-1
		return self.__Line[idx]

	def __Row_Val(self):
		Values=[]
		for Row_id in self.__Permutation_Array:#range(len(self.__Line)):
			ret_val=0
			i=0
			for Col in reversed(range(len(self.__Line))):
				ret_val+=decode(self[Row_id,Col],i)
				i+=1
			Values.append([ret_val,Row_id])
		return Values
	def Get_Values(self):
		return self.__Values
	def Get_Permutation():
		return self.__Permutation_Array
	def Permutation_update(self,Permutation):
		self.__Permutation_Array=Permutation[:]
#	def Size(self):
#		return len(self.__Line)
#	def Col(self,Col_id):
#		return [self[row_id,Col_id] for row_id in range(len(self.__Line))]
