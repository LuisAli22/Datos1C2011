import sys
import os
from Definitions import* 
SIZE_MEM = 10000
class Mem():
	def __init__(self,List):
		self.__Mem=List
		self.__min=find_min(self.__Mem)
	def __setitem__(self, idx, value): 
		self.__Mem[idx] = value

	def __len__(self):	
		return len(self.__Mem)
	def append(self,value):
		if (value<self.__min) or (len(self.__Mem)==0):
			self.__min=value
		self.__Mem.append(value)

	def remove(self,elem):
		self.__Mem.remove(elem)
		if (elem==self.__min)and(len(self.__Mem)>0):
			self.__min=find_min(self.__Mem)
	def get_minor(self):
		return self.__min
	def get_mem(self):
		return self.__Mem
	def update(self,List):
		self.__Mem=List[:]
		self.__min=find_min(self.__Mem)
	
	
