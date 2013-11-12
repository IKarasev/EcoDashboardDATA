from random import *

def get_final_set(iterations):
		report=open("report_final.txt","w")
		line = "{0};{1};{3};{4};{5};{6};{7};\n"
		report.write('#;air;water;land;waste;energy;energy;construction;index;\n')
		args = []
		
		print("Input indicators(value or \"r\" for random.")
		print("air water land waste energy construction")
		
		while len(args) != 6:
			args = input("> ").split(" ")
			if len(args) != 6:
				print("ERROR: 6 values are required. ",len(args),"are inputed")
		for i in range(1,iterations+1):
			air = def_value(args[0],1,10)
			water = def_value(args[1],1,10)
			land = def_value(args[2],1,10)
			waste = def_value(args[3],1,10)
			energy = def_value(args[4],1,10)
			construction = def_value(args[5],1,10)
			index = get_index(air,water,land,waste,energy,construction);
			print("iteration ",i,":  complite", end=" - ")
			report.write(line.format(i,air,water,land,waste,energy,construction,index))
			print("recorded")

def get_index(air,water,land,waste,energy,construction):
	return air+water+land+waste+energy+construction

def def_value(val,min,max):
	if val == "r":
		return randint(min,max)
	else:
		return int(val)

if __name__== "__main__":
	import sys
	get_final_set(int(sys.argv[1]))

