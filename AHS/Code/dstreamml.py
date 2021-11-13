from __future__ import print_function

import sys
import json
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pandas as pd 
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.classification import NaiveBayesModel

sc = SparkContext(master="local[2]",appName="PythonStreamingKafkaWordCount")
ssc = StreamingContext(sc,10)
kafkaParams = {"metadata.broker.list": "localhost:9092"}

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")

kvs = KafkaUtils.createDirectStream(ssc,["test"],kafkaParams=kafkaParams)
def sendRecord(record):
    if(type(record)==tuple):
        model = NaiveBayesModel.load("models/bayes.model")
        model.transform(data).show()
    print(type(record))

kvs.foreachRDD(lambda rdd: rdd.foreach(sendRecord))



kvs.foreachRDD(sendRecord)

ssc.start()
ssc.awaitTermination()