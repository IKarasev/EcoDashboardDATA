if __name__=="__main__":
	import tools
	import sys
	indicators = tools.input_indicators(sys.argv[1])
	weights = tools.input_weights(sys.argv[1])
	if indicators == "error" or weights == "error":
		print("No such inex name")
	else: 
		tools.get_index_set(sys.argv[1],sys.argv[2],indicators,weights)
