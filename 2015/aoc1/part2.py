with open('input') as input:
	poziom = 0
	krok = 0
	for line in input:
		for char in line:
			if poziom == -1:
				print(poziom)
				print(krok)
				break
			elif char == "(":
				poziom += 1
				krok += 1
			else:
				poziom -= 1
				krok += 1