from Definitions import*
from Estructurado import*
class Move_to_front_Estructurate():
	def __init__(self,Matrix):
		self.__Matrix=Matrix
		self.__Y=[]
#		self.__Res=[]
		self.__Estructurado=Modelo_Estructurado()
		
	def run(self,path_file):
		col=self.__Matrix.Get_Col(0)
		self.__Y=list(set(col))
		fichero=Open_File(path_file,"r")
		Line=fichero.readline()
		fichero.close()
		for car in Line[:-1]:
			aux_List=[car]
#			self.__Res.append(self.__Y.index(car))
			self.__Estructurado.run(self.__Y.index(car))
			self.__Y.remove(car)
			self.__Y=aux_List + self.__Y
		print "Resultado final: ","%.20f"% self.__Estructurado.Get_res_number()	
#		return self.__Res
