import sys
import os
from Definitions import* 
SIZE_MEM = 100000
class Mem():
	def __init__(self,Matrix):
		self.__Mem={}
		self.__col=Matrix.Get_Actual_col()
		if Matrix.There_Are_No_Repeated_Rows():
			Top=min(SIZE_MEM,Matrix.Get_Range())
			it_values=range(Top)
		else:
			it_values=Matrix.Get_Repeated_Rows_Actual_Elem()[:SIZE_MEM]
#		print "it_values: ",it_values
		for row in it_values:
#			print "Matrix[",row," ,",self.__col,"]= ",Matrix[row,self.__col]
			self.__Mem[row]=ord(Matrix[row,self.__col])
#		print "---------------"
		self.__min_pos=find_min(self.__Mem)
		
	def __getitem__(self,key):
#		print self.__Mem
#		print "Busco Key",key
		return self.__Mem[key]
	def __setitem__(self, idx, value): 
#		print "Valor: ",value
#		print "Mem: ",self.__Mem
#		print "Pos_min: ",self.__min_pos
		if (len(self.__Mem)==0) or (value<self.__Mem[self.__min_pos]):
			self.__min_pos=idx
		self.__Mem[idx] = value

	def __len__(self):	
		return len(self.__Mem)
#	def append(self,value):
#		if (value<self.__min) or (len(self.__Mem)==0):
#			self.__min=value
#		self.__Mem.append(value)
	def __delitem__(self,key):
		del self.__Mem[key]
		if (key==self.__min_pos)and(len(self.__Mem)>0):
			self.__min_pos=find_min(self.__Mem)
#	def remove(self,elem):
#		self.__Mem.remove(elem)
#		print elem
#		print self.__Mem
#		del self.__Mem[elem]
#		if (elem==self.__min)and(len(self.__Mem)>0):
#			self.__min=find_min(self.__Mem)
	def get_minor_pos(self):
		return self.__min_pos
	def get_mem(self):
		return self.__Mem
	def update(self,Dict):
#		print "MEM ANTES: ",self.__Mem
#		print "Voy a actualizar a: ",Dict
#		self.__Mem=Dict[:]
		self.__Mem.update(Dict)
#		print "MEM DESPUES: ",self.__Mem
		self.__min_pos=find_min(self.__Mem)
#		print "El menor es: ",self.__min_pos
	
	
