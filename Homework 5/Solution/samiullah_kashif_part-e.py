import sys
from pyspark import SparkContext
from operator import add

sc1 = SparkContext(appName="inf551")

lines1 = sc1.textFile('product.txt')

product_price = lines1.map(lambda x: x.split(',')).map(lambda x: (x[3],x[1]))

rdd1 = product_price.aggregateByKey((0.0,0), lambda U,v: (U[0]+float(v),U[1]+1), lambda U1,U2: (U1[0] + U2[0], U1[1] + U2[1]))

rdd1 = rdd1.sortByKey()

output1 = rdd1.mapValues(lambda v: v[0]/v[1]).collect()

for v in output1:
   print '%s,%.2f' %(v[0], v[1])
