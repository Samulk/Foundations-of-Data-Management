#writing this code for extracting data from lax.json
#as specified by user input token strings

#importing this to handle command line arguments
import sys

#for handling queries related to database
import mysql.connector


#function that print the names of the candidates for a particular year
def print_candidate():

   if len(sys.argv) == 1:
   	print 'No input arguments given on the console'
   	print 'Please provide the year for which you want to see the candidates'
   	return
   
   year = sys.argv[1]
   cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
   cursor = cnx.cursor()
   
   query = "SELECT candidate_d, candidate_r FROM Elections where year = " + year
   cursor.execute(query)
   row = cursor.fetchone()
   
   
   if not row:
      print "No record found!!!"     
   else:
      print "democrat: " + row[0]
      print "republican: " + row[1]
      
   
   cursor.close()
   cnx.close()
   
print_candidate()
