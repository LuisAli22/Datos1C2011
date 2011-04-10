class usage_error():
	pass
class File_Error():
	def __init__(self,filename):
		self.__filename=filename
	def Get_FileName(self):
		return self.__filename
