import csv
import os
from Definitions import*
from Estructurado import*
from conversor import* 
class Move_to_front_Estructurate():
	def __init__(self,Matrix):
		self.__Matrix=Matrix
		self.__Y=[]
		self.__Estructurado=Modelo_Estructurado()
		
	def run(self,path_file):
		col=self.__Matrix.Get_Col(0)
		self.__Y=list(set(col))
		fichero=Open_File(path_file,"r")
		fichero_exit=Open_File(os.getcwd()+"/lala.txt."+GROUP_NUMBER,"a+")
		reader = csv.reader(fichero)
		for row in reader:
			num=int(row[0])
			aux_List=[encode(num)]
			self.__Estructurado.run(self.__Y.index(encode(num)),fichero_exit)
			self.__Y.remove(encode(num))
			self.__Y=aux_List + self.__Y
		fichero_exit.write(str(self.__Estructurado.Get_res_number()))	
		fichero_exit.write("\tI="+str(self.__Matrix.Get_Init())+NEW_LINE_CHAR)
		fichero_exit.close()
		fichero.close()
		os.remove(path_file)
#		print "Resultado final: ","%.20f"% self.__Estructurado.Get_res_number()	
