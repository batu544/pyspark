from pyspark.sql import SparkSession

def spark_read():
        spark = SparkSession.builder \
                .appName('test') \
                .getOrCreate()
        return spark


def create_df(spark):
        df = spark.createDataFrame(data=[('Mike', 30), ('Sam', 20)], schema=['name', 'age'])
        return df


if __name__ == "__main__":
        spark = spark_read()
        dff = create_df(spark)
        dff.show()