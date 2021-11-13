import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
spark = SparkContext(conf = conf)

allfiles =  spark.read.option("header","false").csv("C:/SparkStreamingg/SparkStreamingg/part-*.csv")
 
# Output as CSV file
allfiles.coalesce(1).write.format("csv").option("header", "false").save("C:/SparkStreamingg/single_csv_file/")