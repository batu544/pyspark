class Ingest:
    def __init__(self,spark):
        self.spark = spark

    def ingest_data(self):
        print("Ingest process started ")
        print(self.spark.sparkContext.getConf().getAll())
