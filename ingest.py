class Ingest:
    def __init__(self,spark):
        self.spark = spark

    def ingest_data(self):
        print("Ingest process started ")
        #print(self.spark.sparkContext.getConf().getAll())
        self.permDF = self.spark.read.csv("/home/prasanta/Downloads/PERM_Disclosure_Data_FY2021_Q3.csv"
                                     , inferSchema=True
                                     ,header=True)
        #self.permDF.printSchema()
        #self.permDF.select('CASE_STATUS').distinct().show()
        return self.permDF
