import sys
import os
from BlockSorting import*
from Exceptions import*
N_ARGS = 2	
Block_Size = 8
POS_FILE_ARG= 1

def open_file():
	fd=0
	if (len(sys.argv) != N_ARGS):
		raise usage_error()
	try:
		fd=open(sys.argv[POS_FILE_ARG],'r')
	except IOError :
		raise File_Error(sys.argv[POS_FILE_ARG])
	return fd
try:
	my_file=open_file()
	Line=my_file.read(Block_Size)
	while Line:	
		BS=BlockSorting(Line)
		BS.run()
		Line=my_file.read(Block_Size)
	my_file.close()	

except usage_error:
	print """
	Usage:
	python ej.py [data path]
	"""
except File_Error,e :
	print 'No puede abrir ',e.Get_FileName()

