from random import *

#
#	Function that wright down the output in file
#
def get_index_set(index_name, iterations, indicators, weights):
	report=open("report_"+index_name+".txt","w")
	report.write("#;");
	for i in iterations.keys:
		report.write(i+";")
	report.write("\n")
	line = ""
	
	for i in range(0,len(indicators)):
		weights[i] = int(weights[i])
	
	for i in range(0,iterations):
		for n in range(0,len(indicators)):
			indicators[n] = def_value(indicators[n],0,100)
		index = get_index(indicators,weights);
		print("iteration ",i,":  complite", end=" - ")
		
		print("recorded")

#
#	function to count regular index
#	input: indicators[] - list of indicators values
#		   weights[] - list of values of weights of indicators
#
def count_index(indicators,weights):
	index = 0
	if len(indicators) == len(weights):
		for i in range(0,len(indicators)):
			index = index + indicators[i]*weights[i]
		return index
	else:
		print("The numbber of weights does not match the number of weights")

#
#	Function to define the value of the string:
#	if value is a number, function returns int of this number
#	if value is "r", function returns random number from min to max
#
def def_value(value,min,max):
	if value == "r":
		return randint(min,max)
	else:
		return int(value)
