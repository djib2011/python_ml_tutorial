def verbose_print(data):
	typ = data.__class__.__name__
	ln = len(data)
	for i in range(ln):
		j = i + 1 
		if j==1: print('The 1st element in the {} is: {}'.format(typ, data[i]))
		elif j==2: print('The 2nd element in the {} is: {}'.format(typ, data[i]))
		elif j==3: print('The 3rd element in the {} is: {}'.format(typ, data[i]))
		else: print('The {}th element in the {} is: {}'.format(j, typ, data[i]))

if __name__ == '__main':
	print('module used as script')
