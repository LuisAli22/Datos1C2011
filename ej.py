import sys
import os
from Replacement import* 
from Optimal_Merge import*

N_ARGS = 2	
Block_Size = 10
Mem_Size = 3
class usage_error():
	pass
def Ordenate(Line,List_Cant_Reg,path):
	Rep_sel=Replacement(List_Cant_Reg,path)
	for i in range(len(Line)-1):	
		key=encode(Line[1:]+Line[0])
		Rep_sel.Store(key)
		Line=new_Line
	if (Rep_sel.Still_Someone_freeze()):
		Rep_sel.unfreeze()
	Rep_sel.end_data()	

def Create_path():
	path = os.path.join(os.getenv('HOME'), "Compress_Tmp")
	if not os.path.exists(path):
		os.makedirs(path)
	return path
def block_sorting(Line):
	List_Cant_Reg=[]
	path=Create_path()
	Ordenate(Line,List_Cant_Reg,path)
	My_Merge=Merge(Replacement.partition,List_Cant_Reg,path)
	My_Merge.Optimal_Merge()

def open_file():
	if (len(sys.argv) != N_ARGS):
		raise usage_error()
	return open(sys.argv[1],'rbu')
try:
	my_file=open_file()
	Line=my_file.readline()#read(Block_Size)
	block_sorting(Line[:-1])	
except usage_error:
	print """
	Usage:
	python ej.py [data path]
	"""
except IOError:
	print 'No puede abrir ',sys.argv[1]

