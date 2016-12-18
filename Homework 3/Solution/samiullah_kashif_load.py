#writing this code for extracting data from lax.json
#as specified by user input token strings

#importing this to handle command line arguments
import sys

#for handling queries related to database
import mysql.connector

#importing this to load the election data from json files and then insert them in the database
import json

#we will use this to get the names of the files from the directory
from os import listdir
from os.path import isfile, join

#function that inserts the candidates name in the database
def insert_candidates(year, candidate_d, candidate_r):
   cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')

   cursor = cnx.cursor()

   query = "INSERT INTO Elections(year, candidate_d, candidate_r) VALUES(%s,%s,%s)"

   data_query = (year,candidate_d,candidate_r)
   cursor.execute(query,data_query)

   cnx.commit()

   cursor.close()
   cnx.close()

#function that will insert the electoral and popular results of a state
def update_state_results(year, state_name, electoral_d, electoral_r, popular_d, popular_r):
   cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')

   cursor = cnx.cursor()

   query = "UPDATE Elections SET " + state_name + "_electoral_d = %s, " + state_name+ "_electoral_r = %s, " + state_name+ "_popular_d = %s, " + state_name+ "_popular_r = %s WHERE year = %s"
   
   data_query = (electoral_d,electoral_r,popular_d, popular_r,year)
   cursor.execute(query,data_query)

   cnx.commit()

   cursor.close()
   cnx.close()



#function for handling user requests
def DataLoading():
   if len(sys.argv) == 1:
		print 'No input arguments given on the console'
		print 'Please provide the path to the json files'
		return
	
   #if len(sys.argv) == 2:
	#	no_args = True
   #else:
   #   no_args = False
	
	#get the path of the json files from the system arguments
   path = sys.argv[1]
   #this will store all the names of the files inside the directory
   file_names = [f for f in listdir(path) if isfile(join(path, f))]
   
   #looping over the files one by one
   for filename in sorted(file_names):
      #print filename
      try:
         #opening json file in read mode for reading data 
         f = open(path+'/'+filename, 'r')
      except IOError as e:
         print "File could not be opened!!!"
         return
      
      #extracting the name of the year from file name
      year = filename[0:4]
      #print year      
      #loading data from file into data object
      election_data = json.load(f)
      #extracting the name of the candidates from the data object
      candidate_r = election_data["candidates"]["republican"]
      candidate_d = election_data["candidates"]["democrat"]
      
      insert_candidates(year,candidate_d, candidate_r)
      
      #getting the list of all the states in the election
      state_names = (election_data["votes"].keys())
      #print len(state_names)
      
      #iterating over each state
      for state in state_names:
         #setting all variables to 0 so that there is no junk data
         electoral_d = 0
         electoral_r = 0
         popular_d = 0
         popular_r = 0
         
         #checking if the data exists for electoral elections
         if "electoral" in election_data["votes"][state]:
            electoral_results = election_data["votes"][state]["electoral"]
            electoral_d = electoral_results["democrat"]
            electoral_r = electoral_results["republican"]
         
         #checking if the data exists for popular elections
         if "popular" in election_data["votes"][state]:
            popular_results = election_data["votes"][state]["popular"]
            popular_d = popular_results["democrat"]
            popular_r = popular_results["republican"]
      
         update_state_results(year, state, electoral_d, electoral_r, popular_d, popular_r)
      f.close()
	
DataLoading()
