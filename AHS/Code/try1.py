from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
import pandas as pd 

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "test") \
  .load()

df1 = df.selectExpr("CAST(value AS STRING) as json")

df1.writeStream.format("txt").outputMode("complete").option("path", "/SparkStreamingg").option("checkpointLocation", "/SparkStreamingg").start()
df1.writeStream.format("console").option("truncate","false").trigger(processingTime='30 seconds').start().awaitTermination()
