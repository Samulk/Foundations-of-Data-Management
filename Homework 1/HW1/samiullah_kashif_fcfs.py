#this function implements the First Come First Serve algorithm
#of disk scheduling algorithms

import sys #adding this to handle the command line arguments


def fcfs():
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
	#print 'Length of tokens are: ' , len(tokens) 

	for token in tokens:
		number_of_seeks += abs(head_position - int(token))
		head_position = int(token)
		
	f.close()

	#print "Total tracks traversed: ", number_of_seeks
	print number_of_seeks

fcfs()
