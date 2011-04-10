import os
from FileManagement import* 

CANT_VIAS = 4
POS_CANT_REG=0
POS_FILE_PATH=1
PREFIX="/Aux"

class Merge(FileManagement):
	def __init__(self,List,path):
		FileManagement.__init__(self,List,path)
		self.__res={}
		self.__arch_num=0
		self.__count=0
		self.__init_File()
		
	def __init_File(self):
		self.__arch_num+=1
		self.__count=0	
		self.__Actual_Part=Open_File(self.Get_path()+PREFIX+str(self.__arch_num)+EXTENSION,"w")

	def __Get_Minor_Part(self):
		for i in range(CANT_VIAS-1):
			if(len(self.Get_File_list())>0):
				path_file=min(self.Get_File_list(),key=self.Get_File_list().get)
				Cant_Regs=self.Get_File_list().pop(path_file)
				self.__res[path_file]=[Cant_Regs,Open_File(path_file, 'r')]
			else:
				break
	def __Close_and_Store_exit_file_as_Entry(self):
		self.Get_File_list()[self.Get_path()+PREFIX+str(self.__arch_num)+EXTENSION]=self.__count
		self.__Actual_Part.close()

	def __send_to_exit_file(self,Data):
		self.__count=len(Data)
		while(len(Data)>0):
			num=min(Data)
			Data.remove(num)
			self.__Actual_Part.write(str(num)+NEW_LINE_CHAR)
		if (len(self.__res)==0):
			self.__Close_and_Store_exit_file_as_Entry()

	def __delete_completed_files_from_res(self,completed):
		for elem in completed:
			del self.__res[elem]

	def __Close_and_remove_file_from_disk(self,fichero,path,completed=[]):
		fichero.close()
		os.remove(path)
		completed.append(path)	
	
	def __Process_Entry_Files(self):
		completed=[]
		Data=[]
		path_file=min(self.__res,key=self.__res.get)
		Cant_Regs=self.__res.get(path_file)
		reg_num=Cant_Regs[POS_CANT_REG]
		for key,val in self.__res.iteritems():
			Data+=[int(x) for x in val[POS_FILE_PATH].readlines(reg_num)]
			val[POS_CANT_REG]-=reg_num
			if val[POS_CANT_REG]==0:
				self.__Close_and_remove_file_from_disk(val[POS_FILE_PATH],key,completed)						
		self.__delete_completed_files_from_res(completed)
		return Data
		
	def __write_remaining_regs_to_exit_file(self):
		path_file=min(self.__res,key=self.__res.get)
		Cant_Regs=self.__res.pop(path_file)
		List=Cant_Regs[POS_FILE_PATH].readlines()
		self.__Actual_Part.writelines(List)
		self.__count+=len(List)
		self.__Close_and_Store_exit_file_as_Entry()
		self.__Close_and_remove_file_from_disk(Cant_Regs[POS_FILE_PATH],path_file)
	
	def __Process_File(self):
		while (len(self.__res)>0):
			Data=self.__Process_Entry_Files()
			self.__send_to_exit_file(Data)
			if (len(self.__res)<=1):
				if (len(self.__res)==1):
					self.__write_remaining_regs_to_exit_file()
				if len(self.Get_File_list())>1:
					self.__init_File()		
		
	def Optimal_Merge(self):
		while len(self.Get_File_list())>1:
			self.__Get_Minor_Part()
			self.__Process_File()
		return self.Get_File_list().items()[0][0]
		
		
		
