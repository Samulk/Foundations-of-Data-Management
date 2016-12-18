import sys
from pyspark import SparkContext
from operator import add

sc1 = SparkContext(appName="inf551")

lines1 = sc1.textFile('person.txt')

people_in_los_angeles = lines1.map(lambda x: x.split(',')).filter(lambda x: "los angeles" in x[2])

final_answer1 = people_in_los_angeles.map(lambda x: x[0]).map(lambda y: (y,1)).sortByKey()

output1 = final_answer1.collect()

#sc2 = SparkContext(appName="inf552")

lines2 = sc1.textFile('purchase.txt')
#lines2 = sc2.textFile('purchase.txt')

bought_from_john = lines2.map(lambda x: x.split(',')).filter(lambda x: "john" in x[1])

final_answer2 = bought_from_john.map(lambda x: x[0]).map(lambda y: (y,1)).reduceByKey(add)

output2 = final_answer2.collect()

answer = final_answer1.join(final_answer2).sortByKey().collect()

#for v in output1:
#    print '%s %s' %(v[0],v[1])
    
#for v in output2:
#    print '%s %s' %(v[0],v[1])

for v in answer:
   print v[0]
