def get_indicators_names(name):
	if name == "final":
		return "air;water;land;waste;energy;construction;"
	elif name == "air":
		return "ind 1;ind 2;ind 3;"
	elif name == "water":
		return "ind 1;ind 2;ind 3;"
	elif name == "land":
		return "ind 1;ind 2;ind 3;"
	elif name == "waste":
		return "ind 1;ind 2;ind 3;"
	elif name == "energy":
		return "ind 1;ind 2;ind 3;"
	elif name == "construction":
		return "ind 1;ind 2;ind 3;"
	else:
		print("No such index name")
