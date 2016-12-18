#writing this code for extracting data from lax.json
#as specified by user input token strings

#importing this to handle command line arguments
import sys

#for handling queries related to database
import mysql.connector


#function that print the names of the candidates for a particular year
def print_candidate():

   if len(sys.argv) < 4:
   	print 'Not enough input arguments given on the console'
   	print 'You should provide 3 arguments in the format: <year> <candidate name> <state>'
   	return
   
   year = sys.argv[1]
   candidate = sys.argv[2]
   state_name = sys.argv[3]
   sate_name = state_name.upper()
   party = ""
   cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
   cursor = cnx.cursor()
   
   query = "SELECT candidate_d, candidate_r, " + state_name + "_electoral_d, " + state_name + "_electoral_r, " + state_name + "_popular_d, " + state_name + "_popular_r FROM Elections where year = " + year
   cursor.execute(query)
   row = cursor.fetchone()
   
   
   if not row:
      print "No record found!!!"     
   else:
      if candidate.upper() == row[0].upper():
         party = "democrat"
      elif candidate.upper() == row[1].upper():
         party = "republican"
      else:
         print "Candidate name not found in database!!!"
         return
      
      if party == "democrat":
         print "EV: " + str(row[2]) + "; PV: " + str(row[4])
      else:
         print "EV: " + str(row[3]) + "; PV: " + str(row[5])
      #print "democrat: " + row[0]
      #print "republican: " + row[1]
      
   
   cursor.close()
   cnx.close()
   
print_candidate()
