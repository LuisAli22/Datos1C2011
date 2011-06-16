import sys
import math
from Exceptions import*
BASE=2
EXTENSION=".txt"
NEW_LINE_CHAR="\n"
TAB="\t"
#COMA=","
POS_IDX=1
POS_VAL=0
N_ARGS = 2	
GROUP_NUMBER="02"

def Open_File(filename,mode):
	ret_val=0
	if (len(sys.argv) != N_ARGS):
		raise usage_error()
	try:
		ret_val=open(filename,mode)
	except IOError :
		raise File_Error(filename)
	return ret_val
def find_min(List):
	minor=List[0]
	for i in range(1,len(List)):
		if List[i]<minor:
			minor=List[i]
	return minor
def Get_extremeValues(Level_id):
	return math.floor(math.pow(BASE,Level_id-1)),math.pow(BASE,Level_id)-1

