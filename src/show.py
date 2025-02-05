from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName('test') \
        .getOrCreate()

df = spark.createDataFrame(data=[('Mike',30),('Sam',20)], schema=['name', 'age'])

df.show()
