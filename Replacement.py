import sys
import Buffer
SIZE_MEM = Buffer.SIZE_MEM

class Replacement():

	partition=0

	def __init__(self, List,path):
		self.__path=path
		self.__Actual_Part=open(self.__path+"/p"+str(Replacement.partition)+".dat","w")
		self.__Params=List
		self.__Frozen_List=[]
		self.__count=0;
		self.__Mem_idx=0
		self.__Last_in_Partition=0
		self.__Mem=Buffer.CBuffer()
		
	def Close():
		self.__Params +=[self.__count,self.__path+"/p"+str(partition)+".dat"]
		self.__Actual_Part.close()
		self.__count=0
		
	def __del__(self):
		Close()
			
	def Store(key):
		if (self.__Mem_idx<SIZE_MEM):
			self.__Mem[self.__Mem_idx]=key
			self.__Mem_idx +=1
		else:
			Replacement_Selection(key)

	def Get_Minor():
		Pos_Minor=0
		minor=self.__Mem[Pos_Minor]
		for i in range(1,SIZE_MEM-1):
			if ((self.__Mem[i]<minor) and (self.__Mem[i] not in self.__Frozen_List)):
				minor=self.__Mem[i]
				Pos_Minor=1
		return Minor,Pos_Minor

	def All_Frozen():
		return (len(self.__Frozen_List)==SIZE_MEM)

	def enable_new_partition():
		Close()
		partition+=1
		self.__Last_in_Partition=0
		self.__Actual_Part=open(self.__path+"/p"+str(partition)+".dat","w")

	def unfreeze():
		enable_new_partition()
		self.__Frozen_List=[]

	def end_data():
		for i in range(0,SIZE_MEM-1):
			Replacement_Selection(0)
			self.__Frozen_List.append(0)

	def Replacement_Selection(key):
		Expulse=False
		while (not Expulse):
			minor,PosMinor=Get_Minor()
			if (self.__Last_in_Partition>minor):
				self.__Frozen_List.append(minor)
				if (All_Frozen()):
					unfreeze()
			else:
				self.__Actual_Part.write(str(minor)+"\n")
				self.__count +=1
				Expulse=True
		self.Mem[Pos_Minor]=key

	def Still_Someone_freeze():
		return (len(self.__Frozen_List)>0)
