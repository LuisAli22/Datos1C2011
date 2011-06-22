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
		self.__stack_repeated=[]
		self.__written_lines=0
		self.__file_id=0
		self.__First_Time=True
		self.__path = os.path.join(os.getenv(HOME),TEMP_FOLDER )
		if not os.path.exists(self.__path):
			os.makedirs(self.__path)
		self.__name_file_res=self.__path+"/Loc.txt"

	def __Process_file(self,file_name):
		fd=Open_File(file_name,"r")
		My_Dict={}
		csv_file=csv.reader(fd)
		for row in csv_file:
			My_Dict[row[0]]=row[1]
#			print row[0],",",row[1]
		fd.close()
		return My_Dict
	def __Repeated_values(self,List):
		return len(set(List))<len(List)
	def __Set_Last_and_Store_Alone(self,row,lonely):
#		print "lonely tiene: ",lonely
#		print "Guardo en lonely: ",row[1]
#		self.__alone_in_course=True
		lonely.append(row[1])
#		print "lonely queda: ",lonely
		return row[0],row[1],True
	def __Store_Repeated(self,row,alone_in_course,Last_val,Last_pos,aux_rep,repeated,lonely,fd):
		wrote=False
		if Last_pos in lonely:
			lonely.remove(Last_pos)
			aux_rep.append(int(Last_pos))
			if len(lonely)>0:
				self.__Write_To_Final_File(lonely,fd)
				wrote=True
#		print "Agrego: ",row[1]," a ",aux_rep
		aux_rep.append(int(row[1]))
		if wrote:
#			print "Agrego(store repeated): ",aux_rep," a ",repeated
			repeated.append(aux_rep[:])
			aux_rep[:]=[]
			alone_in_course=False
#			print "repetidos..........................: ",repeated
#		print "salgo"
		return alone_in_course
	def __Add_To_Repeated(self,aux_rep,repeated,row,lonely,alone_in_course,Last_val,Last_pos,File_In_Process=True):
		if (len(aux_rep)!=0):
#			print "Agrego(add to repeated): ",aux_rep," a ",repeated
			if (len(repeated)>0):
				repeated[0].append(aux_rep[0])
			else:
				repeated.append(aux_rep[:])
			alone_in_course=False
			aux_rep[:]=[]
		if File_In_Process:
#			print "File in process"
#			print "lonely tiene: ",lonely
#			print "Last_pos: ",Last_pos
			Last_val,Last_pos,alone_in_course=self.__Set_Last_and_Store_Alone(row,lonely)
		return Last_val,Last_pos,alone_in_course
#			lonely.append(row[1])
	def __Bifurcate_repeated_alone(self,row,alone_in_course,Last_val,Last_pos,lonely,repeated,aux_rep,fd):
		if row[0]==Last_val:
			alone_in_course=self.__Store_Repeated(row,alone_in_course,Last_val,Last_pos,aux_rep,repeated,lonely,fd)
		else:
			Last_val,Last_pos,alone_in_course=self.__Add_To_Repeated(aux_rep,repeated,row,lonely,alone_in_course,Last_val,Last_pos)
		return Last_val,Last_pos,alone_in_course
#		print "Salgo del bifurcate"
	def __Get_row_list(self,filename):
		ret_list=[]
		fd=Open_File(filename,"r")
		csv_file=csv.reader(fd)
		for row in csv_file:
			ret_list.append(row[1])
		fd.close()
		return ret_list
	def __Send_To_Alone_Or_Repeated(self,row,alone_in_course,Last_val,Last_pos,repeated,lonely,fd_fin):
#		print "Send_To_Alone_Or_Repeated"
#		First_time=True;
#		val=Last_val
#		pos=Last_pos
		aux_rep=[]
#		fd=Open_File(filename,"r")
#		csv_file=csv.reader(fd)
#		for row in csv_file:
		if self.__First_Time:
#			print "Es first time"
			Last_val,Last_pos,alone_in_course=self.__Set_Last_and_Store_Alone(row,lonely)
#			Last_val=row[0]
#			Last_pos=row[1]
#			print "Agrego a lonely: ",row[1]
#			lonely.append(row[1])
			self.__First_Time=False
		else:
			Last_val,Last_pos,alone_in_course=self.__Bifurcate_repeated_alone(row,alone_in_course,Last_val,Last_pos,lonely,repeated,aux_rep,fd_fin)
#			if len(repeated)>0:
#				break
		Last_val,Last_pos,alone_in_course=self.__Add_To_Repeated(aux_rep,repeated,row,lonely,alone_in_course,Last_val,Last_pos,False)
		return Last_val,Last_pos,alone_in_course
#		fd.close()
#		print "Salgo send to alone or repeated"
	def __Write_To_Final_File(self,lonely,fd):
#		print "Escribo filas: ",lonely
		for elem in lonely:
			car=self.__Matrix[int(elem),self.__Matrix.Get_Range()-1]
			if car !="\n":
				fd.write(car+"\n")
			else:
				fd.write("\n")
			self.__written_lines+=1
			if elem==0:
				self.__Matrix.Set_Init(self.__written_lines)
		lonely[:]=[]
	def __Ordenate(self):
		Rep_sel=Replacement(self.__Partition_List,self.__path,self.__Matrix)
		Res_File=Rep_sel.run()
		if (len(Res_File)==0):
			My_Merge=Merge(self.__Partition_List,self.__path)
			Res_File=My_Merge.run()	
#		Partial_values=self.__Process_file(Res_File)
#		print "Valores parciales: ",Partial_values
#		os.remove(Res_File)
		return Res_File
	def __Ordenate_And_Process(self,repeated,lonely,fd):
#		print "Ordenate and process lonely"
		exit=False
		Res_File=self.__Ordenate()
		self.__Store_filename_in_stack(Res_File)
		self.__Process_Columns(fd)
#		print "ESTOY EN Ordenate and process lonely"
		repeated[:]=[]
		
#		if self.__Repeated_values(Partial_values):
#				self.__Send_To_Alone_Or_Repeated(Partial_values,Res_File,repeated,lonely,fd)
#		else:
#			if self.__Repeated_values(Partial_values)==False:
#			self.__Write_To_Final_File(self.__Get_row_list(Res_File),fd)
#			else:
#				exit=True
#		if len(lonely)>0:
#			print "OJO"
#			self.__Write_To_Final_File(lonely,fd)
#		os.remove(Res_File)
#		return exit
	def __Process_By_Column(self,repeated,lonely,fd):
		self.__Matrix.Set_Num_Block_Repeated(0) 
#		print "Actual Col: ",self.__Matrix.Get_Actual_col()
		while 1:
			all_equal=self.__Matrix.All_equal(self.__First_Time)
			if (self.__Matrix.Out_Of_Range()==True) or (all_equal==False):
				if (all_equal==False):
#					print "DISTINTOS"
					self.__Ordenate_And_Process(repeated,lonely,fd)
				else:
#					print "ME sali del rango"
#					print "QUEDAN REPETIDOS: ",repeated
					self.__Write_To_Final_File(repeated[0],fd)
					repeated[:]=[]
				self.__Matrix.Set_Col(0)
				break
			else:
#				print "TODOS IGUALES"
				self.__Matrix.Inc_Col()
#			self.__Process_Columns(fd)
#			repeated[:]=[]
#			if len(self.__Matrix.Get_Repeated_Rows())>0:
#				repeated.append(self.__Matrix.Get_Repeated_Rows_Actual_Elem()[:])
#		if len(repeated)>0:
#			print "REPETIDOS: ",repeated
#			self.__Matrix.Set_Repeated_Rows(repeated)
#			print "Voy a desempatar....."
#			self.__Process_Columns(fd)
			
	def __Resotore_Data_From_Last_Call(self,stack_repeated,First_Time,init_col,init_num_block_repeated):
		stack_repeated.pop()
		if len(stack_repeated)>0:
			self.__Matrix.Set_Repeated_Rows(stack_repeated[-1])
			if First_Time==False:
				self.__Matrix.Set_Col(init_col)
				self.__Matrix.Set_Num_Block_Repeated(init_num_block_repeated)
			
	def __Process_Columns(self,fd):	
#		print "ENTRO"
		exit=False
		self.__First_Time=True
		alone_in_course=True
		Last_val=0
		Last_pos=0
		lonely=[]
		repeated=[]
		init_num_block_repeated=0
		init_repeated=[]
		init_col=self.__Matrix.Get_Actual_col()
#		if self.__First_Time==False:
#			print "First time FALSE"
#			init_num_block_repeated=self.__Matrix.Get_Num_Block_Repeated() 
#			stack_repeated.append(self.__Matrix.Get_Repeated_Rows()[:])
#			init_col=self.__Matrix.Get_Actual_col()
#			self.__Matrix.Inc_Col()
#			top=self.__Matrix.Get_Quantity_Repeated_Rows()
#		else:
#			top=1
#			print "First time TRUE"
#		print self.__stack_repeated
#		print "Tam stack: ",len(self.__stack_repeated)
		actual_filename=self.__stack_repeated[-1]
#		print "Iter vla: ",self.__stack_repeated[-1]
		if (self.__Matrix.Out_Of_Range()==False):
#			for i in range(top):
			fd_actual=Open_File(actual_filename,"r")
			csv_file=csv.reader(fd_actual)
			for row in csv_file:
#				print row
				Last_val,Last_pos,alone_in_course=self.__Send_To_Alone_Or_Repeated(row,alone_in_course,Last_val,Last_pos,repeated,lonely,fd)
				if len(repeated)>0 and alone_in_course==True:
#					print "Reptidos: ",repeated
					self.__Matrix.Set_Repeated_Rows(repeated)
					self.__Process_By_Column(repeated,lonely,fd)
			if len(lonely)>0:
#				print "OJO"
				self.__Write_To_Final_File(lonely,fd)	
			fd_actual.close()
#		else:
#			print "FUERA DE RANGO"	
		if len(repeated)>0:
#			print "Estoy por salir y quedan repetidos: ",repeated
			self.__Matrix.Set_Repeated_Rows(repeated)
			self.__Process_By_Column(repeated,lonely,fd)	
#		print "SALGO"		
		self.__Matrix.Set_Col(init_col)		
#		print "Actual Col: ",self.__Matrix.Get_Actual_col()		
				
				
				
				
				
				
				
				
				
#				if self.__Process_By_Column(elem,First_Time,repeated,lonely,fd,stack_repeated):
#					equal_rows=True
#					break
#			if equal_rows:
#				self.__Write_To_Final_File(self.__Matrix.Get_Repeated_Rows_Actual_Elem(),fd)
#		if len(stack_repeated)>0:
#			self.__Resotore_Data_From_Last_Call(stack_repeated,First_Time,init_col,init_num_block_repeated)
	def __Delete_Stack_Info(self):
		while 1:
			if (len(self.__stack_repeated)>0):
				os.remove(self.__stack_repeated[-1])
				self.__stack_repeated.pop()
			else:
				break
	def __Store_filename_in_stack(self,old_name):
#		print "Store_filename_in_stack"
		new_name=old_name[:-4]+"_"+str(self.__file_id)+".txt"
		os.rename(old_name,new_name)
		self.__stack_repeated.append(new_name)
		self.__file_id+=1
	def run(self):
		fd_fin=Open_File(self.__name_file_res,"w")
		exit=False
		Res_File=self.__Ordenate()
		self.__Store_filename_in_stack(Res_File)
		self.__Process_Columns(fd_fin)
		self.__Delete_Stack_Info()
		fd_fin.close()
		return self.__name_file_res
