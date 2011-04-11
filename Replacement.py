import sys
from FileManagement import* 
from Definitions import *
from Mem import*
PREFIX_PART="/p"

class Replacement(FileManagement):

	def __init__(self, List,path,Col):
		FileManagement.__init__(self,List,path)
		self.__partition=1
		self.__Last_in_Partition=0
		self.__init_partition()
		self.__Frozen_List=[]
		self.__cant_reg=0
		self.__Mem=Mem(Col[:SIZE_MEM])
		self.__Values=Col[SIZE_MEM:]
		
	def __del__(self):
		self.__Close()		
	def __init_partition(self):
		self.__Actual_Part=Open_File(self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION,"w")
		self.__Last_in_Partition=0
	def __Close(self):
		self.Get_File_list().append([self.__cant_reg,self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION])
		if not self.__Actual_Part.closed:
			self.__Actual_Part.close()
		self.__cant_reg=0

	def __All_Frozen(self):
		return (len(self.__Frozen_List)==SIZE_MEM)

	def __enable_new_partition(self):
		self.__Close()
		self.__partition+=1
		self.__init_partition()

	def __Send_to_Freezer(self,elem):
		self.__Mem.remove(elem)
		self.__Frozen_List.append(elem)
	
	def __Send_to_Partition(self,elem):
		self.__Last_in_Partition=elem[POS_VAL]
		self.__Actual_Part.write(str(elem[POS_VAL])+COMA+str(elem[POS_IDX])+NEW_LINE_CHAR)
		self.__Mem.remove(elem)
		self.__cant_reg +=1
		
	def __unfreeze(self):
		self.__Mem.update(self.__Frozen_List)
		self.__Frozen_List=[]
		self.__enable_new_partition()

	def __Process_Mem(self, value):
		Expulse=False
		while (not Expulse):
			minor=self.__Mem.get_minor()
			Expulse=self.__Send_elem(minor)
		self.__Mem.append(value)

	def __end_data(self):
		while (len(self.__Mem)>0) or (self.__Still_Someone_freeze()):
			if (self.__Still_Someone_freeze() and ((len(self.__Mem)==0))):
				self.__unfreeze()
			minor=self.__Mem.get_minor()
			self.__Send_elem(minor)
	def __Still_Someone_freeze(self):
		return (len(self.__Frozen_List)>0)

	def __Send_elem(self,elem):
		sended_to_Partition=False
		if (self.__Last_in_Partition>elem[POS_VAL]):
			self.__Send_to_Freezer(elem)
			if (self.__All_Frozen()):
				self.__unfreeze()
		else:
			self.__Send_to_Partition(elem)
			sended_to_Partition=True
		return sended_to_Partition


	def run(self):
		for key in self.__Values:
			self.__Process_Mem(key)
		self.__end_data()	
		self.__Close()
		if self.__partition==1:
			return self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION
		return ""
