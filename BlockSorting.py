import csv
from Replacement import* 
from Optimal_Merge import*
from Matrix import*
from conversor import* 
from Definitions import*
import fileinput

PREFIX_NAME="/Loc_File"
TEMP_FOLDER="Compress_Tmp"
HOME='HOME'

class BlockSorting():
	filenumber=0
	def __init__(self,Matrix):
		self.__Matrix=Matrix
		self.__Partition_List=[]
		self.__path = os.path.join(os.getenv(HOME),TEMP_FOLDER )
		if not os.path.exists(self.__path):
			os.makedirs(self.__path)
		
	def __Loc_file(self,Res_File,Original):
		fichero=Open_File(Res_File,"r")
		Pos_Original=0
		Permutation=[]
		First_Val=str(Original)+NEW_LINE_CHAR
		if First_Val in fileinput.input(Res_File):
			self.__Matrix.Set_Init(int(fileinput.filelineno())-1)
		fileinput.close()
		fichero.close()

	def run(self):

		Values=self.__Matrix.Get_Values()
		Rep_sel=Replacement(self.__Partition_List,self.__path,Values)
		Res_File=Rep_sel.run()
		if (len(Res_File)==0):
			My_Merge=Merge(self.__Partition_List,self.__path)
			Res_File=My_Merge.run()	
		self.__Loc_file(Res_File,Values[0])
		return Res_File
