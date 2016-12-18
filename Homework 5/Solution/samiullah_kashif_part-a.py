import sys
from pyspark import SparkContext
from operator import add

sc = SparkContext(appName="inf551")

lines = sc.textFile('person.txt')

people_in_los_angeles = lines.map(lambda x: x.split(',')).filter(lambda x: "los angeles" in x[2])

final_answer = people_in_los_angeles.map(lambda x: x[0]).map(lambda y: (y,1)).sortByKey()

output = final_answer.collect()

for v in output:
    print '%s' %(v[0])

