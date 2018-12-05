from pyspark.sql import SparkSession
from pyspark.sql import Row, SQLContext
from pyspark import SparkContext

def main():
    spark = SparkSession.builder \
     	.master("local") \
    	.appName("Word Count") \
     	.config("com.databricks.spark.csv", "3") \
     	.getOrCreate()
         
    df = spark.read.format('com.databricks.spark.csv').options(header='true', inferschema='true').load("file:///C:/Spark-Python/firstapp/Scripts/source/emp_data.csv")
    type(df)
    df.show()

if __name__ == "__main__":
    main()
