with open('input') as input:
	poziom = 0
	for line in input:
		for char in line:
			if char == "(":
				poziom += 1
			else:
				poziom -= 1
	print(poziom) 