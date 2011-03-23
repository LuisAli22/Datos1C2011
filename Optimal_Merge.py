
CANT_VIAS = 4
POS_idx = 0
POS_Reg_smaller = 1
POS_Regs = 2	
POS_Still_Process = 3
POS_Total_regs=4
POS_Cant_Files = 5
class Merge:
	def __init__(self, Cant_Partition,List,path):
		self.__paths=List
		self.__paths.sort()
		self.__path=path
		self.__handles = [open(Addr[0], 'r') for Addr in self.__paths]
		self.__Total_regs=0
		
	def __del__(self):
		for handle in self.__handles:
			if not handle.closed:
				handle.close()

	def update_control_values(Arg_Val):
		Arg_Val[POS_Still_Process]+=1
		Arg_Val[POS_idx]+=1
		Arg_Val[POS_Reg_smalle]=self.__paths[Arg_Val[POS_idx]][Arg_Val[POS_Cant_Files]] - ArgVal[POS_Reg_smaller]
		self.__Total_regs += Arg_Val[POS_Reg_smaller]
		Arg_Val[POS_Regs]=[]
		
	def update_files(Cant_Files,File_Res):
		for handle in self.__handles[:Cant_Files]:
			handle.close();
		del self.__paths[:Cant_Files]
		del self.__handles[:Cant_Files]
		self.paths +=[self.__Totalregs,self.__path+"/Arch_Salida.dat"]
		self.__handles +=File_Res
	def Process_Entry(Cant_Files,File_Res):
	
		Arg_Val=0,self.__paths[0][Cant_Files],[],1,Cant_Files
		self.__Totalregs=self.__paths[0][Cant_Files]
	
		Files=self.__handles[:Cant_Files]
		Lines_int=[]
		for i in range(Cant_Files):
			for File in Files[Arg_Val[POS_Still_Process]]:
				Lines_int=[int(x) for x in 
						File.readlines(Arg_Val[POS_Reg_smaller])]
				Arg_Val[POS_Regs]+=Lines_int
			Lines_int.sort()
			File_Res.writelines([chr(x) for x in Lines_int])
			update_control_values(Arg_Val)
		update_files(Cant_Files,File_Res)
	def Optimal_Merge():
		File_Res=open(self.__path+"/Arch_Salida.dat","w+")
		Entry_Files=CANT_VIAS-1
		for path in self.__paths:
			Process_Entry(EntryFiles,File_Res)
		File_Res.close()
		
		
		
