from Exceptions import*

EXTENSION=".txt"
NEW_LINE_CHAR="\n"
TAB="\t"
COMA=","
POS_IDX=1
POS_VAL=0

def Open_File(filename,mode):
	ret_val=0
	try:
		ret_val=open(filename,mode)
	except IOError :
		raise File_Error(filename)
	return ret_val
def find_min(List):
	minor=List[0]
	for i in range(1,len(List)):
		if List[i][POS_VAL]<minor[POS_VAL]:
			minor=List[i]
	return minor

