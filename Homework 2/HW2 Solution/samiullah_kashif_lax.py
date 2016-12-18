#writing this code for extracting data from lax.json
#as specified by user input token strings

#importing this to handle command line arguments
import sys

#importing this to handle the lax.json file
import json

#opening the file whose name is lax.json
#assumed to be in the same directory as is the code file

#function for handling user requests
def DataHandling():
   if len(sys.argv) == 1:
		print 'No input arguments given on the console'
		return
	
   if len(sys.argv) == 2:
		no_args = True
   else:
      no_args = False
	
	#this will store the list of input terminals. Can be more than 1
   terminals = []
	
	#this will store the list of years. Can be more than one
   years = []
	
	#user wants arrival info. By default it is false
   arrival = ""
	#user wants departure info. By default it is false
   departure = ""
	
   if no_args == False:
	   args = sys.argv[2].split()
	   #parsing the input arguments
	   for arg in args:
	      if arg[0] == 't' or arg[0] == 'T':
	         #add it to the list of terminals
	         terminals.append(arg)
	      #if this argument contains all digits, it must be year
	      elif arg.isdigit() == True:
	         #add it to the list of years
	         years.append(arg)
	      #user wants arrival data
	      elif arg.lower() == "arrival":
	         #set arrival to 1 denoting get arrival data
	         arrival = "arrival"
	      #user wants departure data   
	      elif arg.lower() == "departure":
	         #set departure to 1 denoting get departure data
	         departure = "departure"

   #user has not specified either arrival or departure which means he needs both
   if arrival == "" and departure == "":
      arrival = "arrival"
      departure = "departure"
   
   #changing terminal names into a standard format
   for i in range(0,len(terminals)):
      if terminals[i].lower() == "t1":
         terminals[i] = "Terminal 1"
      elif terminals[i].lower() == "t2":
         terminals[i] = "Terminal 2"
      elif terminals[i].lower() == "t3":
         terminals[i] = "Terminal 3"
      elif terminals[i].lower() == "t4":
         terminals[i] = "Terminal 4"
      elif terminals[i].lower() == "t5":
         terminals[i] = "Terminal 5"
      elif terminals[i].lower() == "t6":
         terminals[i] = "Terminal 6"
      elif terminals[i].lower() == "tbi":
         terminals[i] = "Tom Bradley International Terminal"
   
   #If user has not given a terminal, then assume all terminals
   if (len(terminals) == 0):
      terminals = ["Terminal 1","Terminal 2","Terminal 3","Terminal 4","Terminal 5","Terminal 6","Tom Bradley International Terminal"]
   
   #if user has not given an year, then assume it is for all years
   if (len(years) == 0):
      years = ["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016"]
   
   
   #print terminals
   #print years
   #print arrival
   #print departure
      
   try:
      #opening json file in read mode for reading data 
      f = open('lax.json', 'r')
   except IOError as e:
      print "File could not be opened!!!"
      return
      
   #loading data from file into data object      
   data = json.load(f)

   #print the number of data rows
   #print len(data["data"])
   
   #for storing total number of passengers which will be the output of the query
   num_passengers = 0
   
   #print "=================================="
   
   #looping over all the records
   for row in data["data"]:
      current_year = row[9][0:4]
      current_terminal = row[10]
      #print row[11]
      #print current_terminal
      if ((arrival == row[11].lower() or departure == row[11].lower()) and (current_year in years) and (current_terminal in terminals)):
         num_passengers = num_passengers + int(row[13])
      #print row[0]

   print num_passengers
DataHandling()
