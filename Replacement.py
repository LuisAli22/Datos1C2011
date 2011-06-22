import sys
from FileManagement import* 
from Definitions import *
from Mem import*
PREFIX_PART="/p"

class Replacement(FileManagement):

	def __init__(self, List,path,Matrix):
		FileManagement.__init__(self,List,path)
		self.__partition=1
		self.__Last_in_Partition=0
		self.__init_partition()
		self.__Frozen_Dict={}
		self.__cant_reg=0
		self.__Mem=Mem(Matrix)
		self.__Matrix=Matrix
#		self.__Values=Col[SIZE_MEM:]
		
	def __del__(self):
		self.__Close()		
	def __Close(self):
		self.Get_File_list().append([self.__cant_reg,self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION])
		if not self.__Actual_Part.closed:
			self.__Actual_Part.close()
		self.__cant_reg=0

	
	def __Send_to_Partition(self,pos_elem):
		self.__Last_in_Partition=self.__Mem[pos_elem]
		self.__Actual_Part.write(str(self.__Mem[pos_elem])+","+str(pos_elem)+NEW_LINE_CHAR)
#		self.__Mem.remove(pos_elem)
		del self.__Mem[pos_elem]
		self.__cant_reg +=1
		
	def __end_data(self):
#		print "End data"
		while (len(self.__Mem)>0) or (self.__Still_Someone_freeze()):
			if (self.__Still_Someone_freeze() and ((len(self.__Mem)==0))):
				self.__unfreeze()
			pos_minor=self.__Mem.get_minor_pos()
#			print "menor key: ",pos_minor
			self.__Send_elem(pos_minor)
	def __Still_Someone_freeze(self):
		return (len(self.__Frozen_Dict)>0)
	
	def __init_partition(self):
		self.__Actual_Part=Open_File(self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION,"w")
		self.__Last_in_Partition=0
		
	def __enable_new_partition(self):
		self.__Close()
		self.__partition+=1
		self.__init_partition()
	
	def __unfreeze(self):
#		print "unfreeze"
		self.__Mem.update(self.__Frozen_Dict)
		self.__Frozen_Dict={}
		self.__enable_new_partition()

	def __All_Frozen(self):
		return (len(self.__Frozen_Dict)==SIZE_MEM)
	
	def __Send_to_Freezer(self,pos_elem):
#		self.__Mem.remove(elem)
		self.__Frozen_Dict[pos_elem]=self.__Mem[pos_elem]
		del self.__Mem[pos_elem]
	def __Send_elem(self,pos_elem):
#		print "send elem: ",self.__Mem[pos_elem]
		sended_to_Partition=False
		if (self.__Last_in_Partition>self.__Mem[pos_elem]):
			self.__Send_to_Freezer(pos_elem)
			if (self.__All_Frozen()):
				self.__unfreeze()
		else:
			self.__Send_to_Partition(pos_elem)
			sended_to_Partition=True
		return sended_to_Partition

	def __Process_Mem(self, value,key):
		Expulse=False
		while (not Expulse):
#			print "Mem: ",self.__Mem
			minor_pos=self.__Mem.get_minor_pos()
#			print "Mado el menor a freezer o particion: ",self.__Mem[minor_pos]
			Expulse=self.__Send_elem(minor_pos)
#		print "Agrego a la memoria el valor: ",value
		self.__Mem[key]=value
	def __Get_Values(self):
		if self.__Matrix.Get_Actual_col()==0:
			return range(SIZE_MEM,self.__Matrix.Get_Range())
		return self.__Matrix.Get_Repeated_Rows_Actual_Elem()[SIZE_MEM:]#self.__Matrix.Get_Quantity_Repeated_Rows()
	def run(self):
#		print "size_mem: ",SIZE_MEM," Rango Matriz:",self.__Matrix.Get_Range()
		it_val=self.__Get_Values()
#		value={}
		for row in it_val:
			value=ord(self.__Matrix[row,self.__Matrix.Get_Actual_col()])
#			print "Value: ",value
			self.__Process_Mem(value,row)
		self.__end_data()	
		self.__Close()
		if self.__partition==1:
			return self.Get_path()+PREFIX_PART+str(self.__partition)+EXTENSION
		return ""
