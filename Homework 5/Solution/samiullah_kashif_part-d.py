import sys
from pyspark import SparkContext
from operator import add

sc1 = SparkContext(appName="inf551")

lines1 = sc1.textFile('product.txt')

names_laptops = lines1.map(lambda x: x.split(',')).filter(lambda x: "laptop" in x[2]).map(lambda x: (x[0],x[2]))

output1 = names_laptops.collect()
    
lines2 = sc1.textFile('purchase.txt')

product_seller = lines2.map(lambda x: x.split(',')).map(lambda x: (x[3],x[1]))

output2 = product_seller.collect()

seller_laptop = product_seller.join(names_laptops).map(lambda x: (x[1][0], (x[1][1]))).groupByKey().keys()

names_cellphones = lines1.map(lambda x: x.split(',')).filter(lambda x: "cell phone" in x[2]).map(lambda x: (x[0],x[2]))

output1 = names_cellphones.collect()
    
lines2 = sc1.textFile('purchase.txt')

product_seller_cp = lines2.map(lambda x: x.split(',')).map(lambda x: (x[3],x[1]))

output2 = product_seller_cp.collect()

seller_cellphone = product_seller_cp.join(names_cellphones).map(lambda x: (x[1][0], (x[1][1]))).groupByKey().keys()


final_answer = seller_laptop.subtract(seller_cellphone).collect()

for v in final_answer:
   print v
