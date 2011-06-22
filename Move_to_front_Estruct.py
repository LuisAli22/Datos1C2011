import csv
import os
import fileinput
from Definitions import*
from Estructurado import*
from conversor import* 
class Move_to_front_Estructurate():
	def __init__(self,Matrix,exit_file):
		self.__Matrix=Matrix
		self.__New_Order={}
		self.__Car_in_Front=""
		self.__Estructurado=Modelo_Estructurado(exit_file)
	def __swap_pos(self,Car,idx):
		car_zero=chr(0) if (self.__Car_in_Front =="") else self.__Car_in_Front			
		self.__New_Order[Car]=0
		self.__New_Order[car_zero]=idx
		
	def __Get_idx(self,Car):
		idx=self.__New_Order[Car] if Car in self.__New_Order.keys() else ord(Car)
		if Car not in self.__New_Order:
			self.__swap_pos(Car,idx);
		return idx
	def run(self,path_file):
		fd=Open_File(path_file,"r")
		car=fd.read(1+len("\n"))
#		print "Pulse una tecla..."
		while car:
#			print "Leo: ",car
			if car !="\n":
				car=car[:-1]#.rstrip('\n')
			num_pos=self.__Get_idx(car);			
			self.__Estructurado.run(num_pos)
			car=fd.read(1+len("\n"))
		if self.__Estructurado.All_data_stored()==False:
			self.__Estructurado.Bit_padding()
		self.__Matrix.Write_Init()
		fd.close()
#		x=input()
		os.remove(path_file)
