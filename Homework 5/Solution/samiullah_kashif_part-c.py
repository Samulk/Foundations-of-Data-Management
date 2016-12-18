import sys
from pyspark import SparkContext
from operator import add

sc1 = SparkContext(appName="inf551")

lines1 = sc1.textFile('product.txt')

products_manufacturer = lines1.map(lambda x: x.split(',')).map(lambda x: (x[3],x[0]))

output1 = products_manufacturer.collect()
    
lines2 = sc1.textFile('company.txt')

company_country = lines2.map(lambda x: x.split(',')).map(lambda x: (x[0],x[2]))

output2 = company_country.collect()

final_answer = products_manufacturer.join(company_country).map(lambda x: (x[1][0], (x[1][1]))).collect()

for v in final_answer:
    print '%s,%s' %(v[0],v[1])
