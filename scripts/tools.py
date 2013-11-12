def get_test(get_index,name,*args):
	
	for i in range(0,len(args)):
		args[i]=define_value(arg[i])
	index = get_index(args);

def define_value(val,min,max):
	if val == "r":
		return randint(min,max)
	else:
		return int(val)
