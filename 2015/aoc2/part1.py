with open('input') as input:
	wynik = 0
	for line in input:
		splitted = line.split('x')
		splitted_int = list(map(int, splitted))
		splitted_int.sort()
		w = splitted_int[0]
		l = splitted_int[1]
		h = splitted_int[2]
		wynik += 2*l*w + 2*w*h + 2*h*l + w*l
	print (wynik)