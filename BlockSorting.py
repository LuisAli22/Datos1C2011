import csv
from StringIO import StringIO
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
		self.__Matrix=Matrix#CMatrix(Line)
		self.__Partition_List=[]
		self.__path = os.path.join(os.getenv(HOME),TEMP_FOLDER )
		if not os.path.exists(self.__path):
			os.makedirs(self.__path)
	def __Get_value_from_line(self,line,permutation):
		num=0
		csv_file = StringIO(line)
		reader = csv.reader(csv_file)
		for row in reader:
			if (len(row)>0):
				num=int(row[0])
				permutation.append(int(row[1]))
		return num
		
	def __Loc_file(self,Res_File,Original):
		fichero=Open_File(Res_File,"r")
		Loc_file_path=self.__path+PREFIX_NAME+str(self.__class__.filenumber)+EXTENSION
		Loc_File=Open_File(Loc_file_path,"w")
		self.__class__.filenumber+=1
		Pos_Original=0
		Permutation=[]
		for line in fileinput.input(Res_File):
			if line.find(str(Original)) >= 0:
				Pos_Original=int(fileinput.filelineno())-1
			num=self.__Get_value_from_line(line,Permutation)
			Loc_File.write(encode(num))
		Loc_File.write(NEW_LINE_CHAR+str(Pos_Original))	
		fichero.close()
		Loc_File.close()
		os.remove(Res_File)
		self.__Matrix.Permutation_update(Permutation)
		return Loc_file_path

	def run(self):

		Values=self.__Matrix.Get_Values()
		Rep_sel=Replacement(self.__Partition_List,self.__path,Values)
		Res_File=Rep_sel.run()
		if (len(Res_File)==0):
			My_Merge=Merge(self.__Partition_List,self.__path)
			Res_File=My_Merge.run()	
		return self.__Loc_file(Res_File,Values[0])
