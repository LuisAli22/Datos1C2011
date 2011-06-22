import os
from FileManagement import* 

CANT_VIAS = 100
POS_CANT_REG=0
POS_FILE_PATH=1
POS_FILE=2
PREFIX="/Aux"

class Merge(FileManagement):
	def __init__(self,List,path):
		FileManagement.__init__(self,List,path)
		self.__res=[]
		self.__arch_num=0
		self.__count=0
		self.__init_File()
		
	def __init_File(self):
		self.__arch_num+=1
		self.__count=0	
		self.__Actual_Part=Open_File(self.Get_path()+PREFIX+str(self.__arch_num)+EXTENSION,"w")

	def __Get_Minor_Part(self):
		for i in range(CANT_VIAS-1):
#			print self.Get_File_list()
			if(len(self.Get_File_list())>0):
				elem=find_min_list(self.Get_File_list())
				path_file=elem[POS_FILE_PATH]
				Cant_Regs=elem[POS_VAL]
				self.Get_File_list().remove(elem)
#				print "Agrego a res: ",path_file
				self.__res.append([Cant_Regs,path_file,Open_File(path_file, 'r')])
			else:
				break
	def __Close_and_Store_exit_file_as_Entry(self):
		self.Get_File_list().append([self.__count,self.Get_path()+PREFIX+str(self.__arch_num)+EXTENSION])
		self.__Actual_Part.close()

	def __send_to_exit_file(self,Data):
		self.__count=len(Data)
		while(len(Data)>0):
			elem=find_min_list(Data)
			Data.remove(elem)
			self.__Actual_Part.write(elem)
		if (len(self.__res)==0):
			self.__Close_and_Store_exit_file_as_Entry()

	def __delete_completed_files_from_res(self,completed):
		for elem in completed:
			self.__res.remove(elem)

	def __Close_and_remove_file_from_disk(self,val,completed=[]):
#		print "Elimino ",val[POS_FILE_PATH]
		val[POS_FILE].close()
		os.remove(val[POS_FILE_PATH])
		completed.append(val)
			
	def __Process_Entry_Files(self):
		completed=[]
		Data=[]
		elem=find_min_list(self.__res)
		path_file=elem[POS_FILE_PATH]
#		print "Porceso: ",path_file
		reg_num=elem[POS_VAL]
#	print "self.__res: ",self.__res
		for val in self.__res:
			Data+=val[POS_FILE].readlines(reg_num)
			val[POS_VAL]-=reg_num
			if val[POS_VAL]==0:
				self.__Close_and_remove_file_from_disk(val,completed)			
		self.__delete_completed_files_from_res(completed)
		return Data
		
	def __write_remaining_regs_to_exit_file(self):
		elem=self.__res.pop()
		path_file=elem[POS_FILE_PATH]
		List=elem[POS_FILE].readlines()
		self.__Actual_Part.writelines(List)
		self.__count+=len(List)
		self.__Close_and_Store_exit_file_as_Entry()
		self.__Close_and_remove_file_from_disk(elem)
	
	def __Process_File(self):
		while (len(self.__res)>0):
			Data=self.__Process_Entry_Files()
			self.__send_to_exit_file(Data)
			if (len(self.__res)<=1):
				if (len(self.__res)==1):
					self.__write_remaining_regs_to_exit_file()
				if len(self.Get_File_list())>1:
					self.__init_File()		
		
	def run(self):
		while len(self.Get_File_list())>1:
			self.__Get_Minor_Part()
			self.__Process_File()
		return self.Get_File_list()[0][POS_FILE_PATH]
		
		
		
