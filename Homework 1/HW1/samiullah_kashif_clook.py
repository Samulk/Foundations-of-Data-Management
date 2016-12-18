#this function implements the First Come First Serve algorithm
#of disk scheduling algorithms

import sys #adding this to handle the command line arguments


def clook():
	if len(sys.argv) < 2:
		print 'File name not given on console'
	i = 0
	number_of_seeks = 0
	filename = ''
	for arg in sys.argv:
		if(i == 1):
			filename = arg

		i+= 1

	#print 'File name is: ', filename
	
	f = open(filename,'r')
	head_position = int(f.readline())

	#print 'Head Position in the start is at: ' , head_position

	line = f.readline()
	
	tokens = line.split()
	int_tokens = [int(i) for i in tokens]
	#print 'Length of tokens are: ' , len(int_tokens)
	#print int_tokens
	
	while len(int_tokens) != 0:
		copy_array = []
		for x in int_tokens:
			if x <= head_position:
				copy_array.append(head_position - x)
			else:
				copy_array.append(float('inf'))
	
		
		if len(int_tokens) == 0:
			break

		if min(copy_array) == float('inf'):
			head_position = max(int_tokens)
			continue
		#print int_tokens
	
		min_index = copy_array.index(min(copy_array))
		min_value = int_tokens[min_index]
		
		#print number_of_seeks
		#print copy_array
		#print min_index
		#print min_value
		#print '###############################################'

		#copy_array[min_index] = float('inf')

		number_of_seeks += abs(head_position - min_value)
		head_position = min_value
		int_tokens.pop(min_index)		
	f.close()

	#print "Total tracks traversed: ", number_of_seeks
	print number_of_seeks

clook()
