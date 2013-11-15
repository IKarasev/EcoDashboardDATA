from indexes import get_indicators_names

#
#	Function that wright down the output in file name reopt_index-name.txt
#	Input:  index_name - nam of the index
#			iterations - number of iterations
#			idicators - list of indicators codes (number or "r")
#			weights - list of weights values
#
def get_index_set(index_name, iterations, indicators, weights):
		line = ""															 # the line to input in file
		indicators_value = []												 # the values of indicators
	# open file
		report=open("report_"+index_name+".txt","w")
	# write titles
		report.write("#;"+get_indicators_names(index_name)+"index;\n");
	# write weights
		report.write("w: ;")
		for i in weights:
			report.write(str(i)+";");
		report.write("\n")
	
	# define values of weights
		for i in range(0,len(indicators)):
			weights[i] = int(weights[i])
	
	# count and write down index for [itertions] number of iterations
		for i in range(1,int(iterations)+1):
			indicators_value.clear()
			for n in range(0,len(indicators)):                            # define values of indicators
				indicators_value.append(def_value(indicators[n],0,100))
				
			index = get_index(indicators_value,weights);                  # count index
			print("iteration ",i,":  complite", end=" - ")                # write down the reults		
		# build line to input in file
			line = str(i)+";"
			for n in indicators_value:
				line = line + str(n)+";"
			line = line + str(index) +";\n"
			report.write(line);
			print("recorded")

#
#	Function to define the value of the string:
#	if value is a number, function returns int of this number
#	if value is "r", function returns random number from min to max
#
def def_value(value,min,max):
	from random import randint
	if value == "r":
		return randint(min,max)
	else:
		return int(value)

#
#	function to count regular index
#	input: indicators[] - list of indicators values
#		   weights[] - list of values of weights of indicators
#
def get_index(indicators,weights):
	index = 0
	if len(indicators) == len(weights):
		for i in range(0,len(indicators)):
			index = index + indicators[i]*weights[i]
		return index
	else:
		print("The numbber of weights does not match the number of weights")
#
#	Function to get indigators names of index "index_name"
#	Output: string - names of indicatros
#

#def get_indicators_names(index_name):
#	if index_name=="final":
#		import final
#		return final.get_indicators_names();

def input_indicators(index_name):
	if index_name == "final":
		print("\nInput indicators(value or \"r\" for random value)")
		indicators = []
		number = len(get_indicators_names(index_name).split(";"))-1
		print(number," values\n")
		print(get_indicators_names(index_name))
		while len(indicators) != number:
			indicators = input("> ").split(" ")
			if len(indicators) != number:
				print("ERROR: ",number," values are required. ",len(indicators),"are inputed. Try again:")
		return indicators
	else:
		return "error" # no such index name

def input_weights(index_name):
	if index_name == "final":
		print("Input weights:")
		weights = []
		number = len(get_indicators_names(index_name).split(";"))-1
		while len(weights) != number:
			weights = input("> ").split(" ")
			if len(weights) != number:
				print("ERROR: ",number," values are required. ",len(weights),"are inputed. Try again:")
		return weights
	else:
		return "error" #no such index name

		