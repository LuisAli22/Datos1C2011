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
def find_min_list(List):
	print List
	minor=List[0]
#	print "Menor inicial: ",minor
	for elem in List[1:]:
		if elem[0]<minor[0]:
			minor=elem
#	print "El menor es: ",minor
	return minor
def find_min(Dict):
#	print "List: ",List 
	pos=Dict.keys()[0]
	minor=Dict[pos]
	for i in Dict.keys()[1:]:
#		print "List[",i,"]: ",List[i],"\tMenor: ",minor
		if Dict[i]<minor:
			minor=Dict[i]
			pos=i
	return pos
def Get_extremeValues(Level_id):
	return math.floor(math.pow(BASE,Level_id-1)),math.pow(BASE,Level_id)-1

