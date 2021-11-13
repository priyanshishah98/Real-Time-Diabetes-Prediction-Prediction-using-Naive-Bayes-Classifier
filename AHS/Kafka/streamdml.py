from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
kafkaParams = {"metadata.broker.list": "localhost:9092"}

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext(appName="NetworkWordCount")
ssc = StreamingContext(sc, 1)
kvs = KafkaUtils.createDirectStream(ssc,["test"],kafkaParams=kafkaParams)
model = NaiveBayesModel.load(sc,"myNaiveBayesModel")

def sendRecord(record):
    data = record[1]
    dataVector = data.split(" ")
    prediction = model.predict(dataVector)
    print(prediction)
    print(type(record[1]))
    print(record[1])

kvs.foreachRDD(lambda rdd: rdd.foreach(sendRecord))
print("Stream Running ")

ssc.start()
ssc.awaitTermination()
