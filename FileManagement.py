from Definitions import*

class FileManagement():
	def __init__(self,List,path):
		self.__File_list=List
		self.__List_Cant_Reg=[]
		self.__path=path
		
	def Get_path(self):
		return self.__path
		
	def Get_List_Reg(self):
		return self.__List_Cant_Reg
	def Get_File_list(self):
		return self.__File_list

#	@classmethod
#	def Open_File(self,filename,mode):
#		ret_val=0
#		try:
#			ret_val=open(filename,mode)
#		except IOError :
#			raise File_Error(filename)
#		return ret_val
