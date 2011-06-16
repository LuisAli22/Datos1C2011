from BlockSorting import*
from Move_to_front_Estruct import*

class Compress():
	def __init__(self,Line,exit_file):
		self.__Matrix=CMatrix(Line,exit_file)
		self.__BS=BlockSorting(self.__Matrix)
		self.__MTF_E=Move_to_front_Estructurate(self.__Matrix,exit_file)
		
	def run(self):
		Loc_file_path=self.__BS.run()
		self.__MTF_E.run(Loc_file_path)
