import sys
import os
SIZE_MEM = 3
class Mem():
	def __init__(self,List):
		self.__Mem=List
		self.__find_min()

	def __setitem__(self, idx, value): 
		self.__Mem[idx] = value

	def __len__(self):	
		return len(self.__Mem)
	def append(self,value):
		if (value<self.__min) or (len(self.__Mem)==0):
			self.__min=value
		self.__Mem.append(value)
	def __find_min(self):
		minor=self.__Mem[0]
		for i in range(1,len(self.__Mem)):
			if self.__Mem[i]<minor:
				minor=self.__Mem[i]
		self.__min=minor

	def remove(self,elem):
		self.__Mem.remove(elem)
		if (elem==self.__min)and(len(self.__Mem)>0):
			self.__find_min()
	def get_minor(self):
		return self.__min
	def get_mem(self):
		return self.__Mem
	def update(self,List):
		self.__Mem=List[:]
		self.__find_min()
	
	
