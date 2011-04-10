from Exceptions import*

EXTENSION=".txt"
NEW_LINE_CHAR="\n"


def Open_File(filename,mode):
	ret_val=0
	try:
		ret_val=open(filename,mode)
	except IOError :
		raise File_Error(filename)
	return ret_val
