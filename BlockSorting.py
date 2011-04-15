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
	def __Get_Permutation(self,fichero,permutation):
		reader = csv.reader(fichero)
		for row in reader:
			if (len(row)>0):
				permutation.append(int(row[1]))
		
	def __Loc_file(self,Res_File,Original):
		fichero=Open_File(Res_File,"r")
		Pos_Original=0
		Permutation=[]
		First_Val=str(Original[POS_VAL])+COMA+str(Original[POS_IDX])+NEW_LINE_CHAR
		K=fileinput.input(Res_File)
		if First_Val in K:
			self.__Matrix.Set_Init(int(fileinput.filelineno())-1)
		self.__Get_Permutation(fichero,Permutation)
		fichero.close()
		self.__Matrix.Permutation_update(Permutation)

	def run(self):

		Values=self.__Matrix.Get_Values()
		Rep_sel=Replacement(self.__Partition_List,self.__path,Values)
		Res_File=Rep_sel.run()
		if (len(Res_File)==0):
			My_Merge=Merge(self.__Partition_List,self.__path)
			Res_File=My_Merge.run()	
		self.__Loc_file(Res_File,Values[0])
		return Res_File
