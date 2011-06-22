import sys
import os
from Exceptions import*
from Compress import*
from Definitions import*

Block_Size = 1000
POS_FILE_ARG= 1

try:
	name_file=sys.argv[POS_FILE_ARG]
	my_file=Open_File(name_file,"rb")
	exit_file=Open_File(os.getcwd()+"/"+name_file+"."+GROUP_NUMBER,"wb")
	Line=my_file.read(Block_Size+len("\n"))
	count=1
	while Line:	
		Line=Line[:-1]#.rstrip('\n')
#		print "proceso bloque N ",count
		count+=1
#		print "linea: ",Line
#		print "Tamanio: ",len(Line)
		if len(Line)>0:
			Compress_file=Compress(Line,exit_file)
			Compress_file.run()
			Line=my_file.read(Block_Size+len("\n"))
	my_file.close()	
	exit_file.close()

except usage_error:
	print """
	Usage:
	python ej.py [data path]
	"""
except File_Error,e :
	print 'No puede abrir ',e.Get_FileName()

