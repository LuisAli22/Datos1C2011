from BlockSorting import*
from Move_to_front import*
from Estructurado import*

class Compress():
	def __init__(self,Line):
		self.__Matrix=CMatrix(Line)
		self.__BS=BlockSorting(self.__Matrix)
		self.__MTF=Move_to_front(self.__Matrix)
		self.__Estructurado=Modelo_Estructurado()
		
	def run(self):
		Loc_file_path=self.__BS.run()
#		print self.__Matrix.Get_Permutation()
		Prior_file_list=self.__MTF.run(Loc_file_path)
		self.__Estructurado.run(Prior_file_list)
