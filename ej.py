import sys
import os
from Exceptions import*
from Compress import*
from Definitions import*

Block_Size = 8
POS_FILE_ARG= 1

try:
	my_file=Open_File(sys.argv[POS_FILE_ARG],"r")
	Line=my_file.read(Block_Size)
	while Line:	
		if len(Line)<Block_Size:
			Line=Line[:-1]
		Compress_file=Compress(Line)
		Compress_file.run()
		Line=my_file.read(Block_Size)
	my_file.close()	

except usage_error:
	print """
	Usage:
	python ej.py [data path]
	"""
except File_Error,e :
	print 'No puede abrir ',e.Get_FileName()

