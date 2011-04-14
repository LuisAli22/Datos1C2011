import math
from Exceptions import*
BASE=2
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
def find_min(List,from_upper=False):
	minor=List[0]
	for i in range(1,len(List)):
		if List[i][POS_VAL]<minor[POS_VAL]:
			minor=List[i]
			if i>0:
				from_upper=True
	return minor
def Get_extremeValues(Level_id):
	return math.floor(math.pow(BASE,Level_id-1)),math.pow(BASE,Level_id)-1

