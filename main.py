from pyspark.sql import SparkSession
import ingest
import transform
import persist


class Pipeline:
    def run_pipeline(self):
        print("Running pipeline")

        ingest_process = ingest.Ingest(self.spark)
        ingest_process.ingest_data()

        transform_proces = transform.Transform()
        transform_proces.transform_data()

        persist_process = persist.Persist()
        persist_process.persist_data()

        return None

    def create_spark_session(self):
        self.spark = SparkSession.builder\
            .master('local[4]')\
            .appName('Data pipeline Test')\
            .getOrCreate()

        return None



if __name__ == "__main__":
    pipeline = Pipeline()

    """Create spark Session
    """
    pipeline.create_spark_session()
    pipeline.run_pipeline()
