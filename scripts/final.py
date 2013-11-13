from random import *

def get_final_set(iterations):
		report=open("report_final.txt","w")
		line = ""
		report.write('#;air;water;land;waste;energy;energy;construction;index;\n')
		indicators = []
		weights = []
		
		print("Input indicators(value or \"r\" for random.")
		print("air water land waste energy construction")
		
		while len(indicators) != 6:
			indicators = input("> ").split(" ")
			if len(indicators) != 6:
				print("ERROR: 6 values are required. ",len(indicators),"are inputed")
		while len(weights) != 6:
			weights = input("> ").split(" ")
			if len(weights) != 6:
				print("ERROR: 6 values are required. ",len(indicators),"are inputed")
		
		for i in range(0,len(weights)):
			weights[i] = def_value(weights[i],0,100)
			
		for i in range(0,iterations):
			for n in range(0,len(indicators)):
				indicators[n] = def_value(indicators[n],0,100)
			index = get_index(indicators,weights);
			print("iteration ",i,":  complite", end=" - ")
			line = str(i) + ";"
			for n in range(0,len(indicators)):
				line  = line + str(indicators[n]) + ";"
			line = line + "/n"
			report.write(line)
			print("recorded")

def get_index(indicators,weights):
	index = 0
	if len(indicators) == len(weights):
		for i in range(0,len(indicators)):
			index = index + indicators[i]*weights[i]
		return index
	else:
		print("The numbber of weights does not match the number of weights")

def def_value(val,min,max):
	if val == "r":
		return randint(min,max)
	else:
		return int(val)

if __name__== "__main__":
	import sys
	get_final_set(int(sys.argv[1]))

