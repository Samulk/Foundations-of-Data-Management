#this function implements the First Come First Serve algorithm
#of disk scheduling algorithms

import sys #adding this to handle the command line arguments


def sstf():
	if len(sys.argv) < 2:
		print 'File name not given on console'
	i = 0
	number_of_seeks = 0
	start_track_number = 0
	end_track_number = 199
	filename = ''
	direction = ''
	previous_direction = ''
	first_step = True
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
		copy_array[:] = [abs(x - head_position) for x in int_tokens]
	
		#print copy_array
		#print int_tokens
	
		min_index = copy_array.index(min(copy_array))
		#min_value = int_tokens[min_index]
		min_value = copy_array[min_index]
		min_orig = int_tokens[min_index]
		copy_array[min_index] = float('inf')

		

		if len(copy_array) > 1:
			smin_index = copy_array.index(min(copy_array))
			smin_value = copy_array[smin_index]
			smin_orig = int_tokens[smin_index]
			copy_array[smin_index] = float('inf')
		else:
			smin_value = ('-inf')

		#print number_of_seeks
		#print min_orig
		#print smin_orig		
		#print int_tokens
		#print min_index
		##print min_value
		#print smin_index
		#print smin_value
		
		#print '###############################################'

		if min_value != smin_value:
			if min_orig <= head_position:
				direction = 'L'
			else:
				direction = 'R'
		
			number_of_seeks += abs(head_position - min_orig)
			head_position = min_orig
			int_tokens.pop(min_index)
		

		if min_value == smin_value and first_step == True:
			distance_from_start = abs(head_position - start_track_number)
			distance_from_end = abs(end_track_number - head_position)

			#print distance_from_start
			#print distance_from_end
			
			if distance_from_start <= distance_from_end:
				direction = 'L'
			else:
				direction = 'R'

			#previous_direction = direction

			if direction == 'L':
				if min_index < smin_index:
					number_of_seeks += abs(head_position - min_orig)
					head_position = min_orig
					int_tokens.pop(min_index)
				else:
					number_of_seeks += abs(head_position - smin_orig)
					head_position = smin_orig
					int_tokens.pop(smin_index)

			if direction == 'R':
				
				if min_index < smin_index:
					#print min_index
					#print min_value
					#print smin_index
					#print smin_value
		
					number_of_seeks += abs(head_position - smin_orig)
					head_position = smin_orig
					int_tokens.pop(smin_index)
					#print number_of_seeks
					#print head_position
					
				else:
					number_of_seeks += abs(head_position - min_orig)
					head_position = min_orig
					int_tokens.pop(min_index)
	

		if min_value == smin_value and first_step == False:
			if direction == 'L': #changed here
				if min_orig < smin_orig:
					number_of_seeks += abs(head_position - min_orig)
					head_position = min_orig
					int_tokens.pop(min_index)
				else:
					number_of_seeks += abs(head_position - smin_orig)
					head_position = smin_orig
					int_tokens.pop(smin_index)

			if direction == 'R':  #changed here
				if min_orig < smin_orig:
					number_of_seeks += abs(head_position - smin_orig)
					head_position = smin_orig
					int_tokens.pop(smin_index)
				else:
					number_of_seeks += abs(head_position - min_orig)
					head_position = min_orig
					int_tokens.pop(min_index)
		
		first_step = False
	f.close()

	#print "Total tracks traversed: ", number_of_seeks
	print number_of_seeks

sstf()
