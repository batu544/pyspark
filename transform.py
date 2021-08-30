class Transform:
    def __init__(self, spark):
        self.spark = spark

    def transform_data(self, df):
        print("Transform started")
        print(df.count())

