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
	def __init__(self,Line):
		self.__Matrix=CMatrix(Line)
		self.__Partition_List={}
		self.__path = os.path.join(os.getenv(HOME),TEMP_FOLDER )
		if not os.path.exists(self.__path):
			os.makedirs(self.__path)
	def __Loc_file(self,Res_File,Original):
		fichero=Open_File(Res_File,"r")
		Loc_File=Open_File(self.__path+PREFIX_NAME+str(self.__class__.filenumber)+EXTENSION,"w")
		self.__class__.filenumber+=1
		Pos_Original=0
#		i=0
		for line in fileinput.input(Res_File):
#			i+=1
			if line.find(str(Original)) >= 0:
				Pos_Original=int(fileinput.filelineno())-1
			Loc_File.write(encode(int(line)))
		Loc_File.write(NEW_LINE_CHAR+str(Pos_Original))	
		fichero.close()
		Loc_File.close()
		os.remove(Res_File)

	def run(self):

		Values=[self.__Matrix.Row_Val(Row_id) for Row_id in range(self.__Matrix.Size()) ]
		Rep_sel=Replacement(self.__Partition_List,self.__path,Values)
		Res_File=Rep_sel.Replacement_Selection()
		if (len(Res_File)==0):
			My_Merge=Merge(self.__Partition_List,self.__path)
			Res_File=My_Merge.Optimal_Merge()	
		self.__Loc_file(Res_File,Values[0])
