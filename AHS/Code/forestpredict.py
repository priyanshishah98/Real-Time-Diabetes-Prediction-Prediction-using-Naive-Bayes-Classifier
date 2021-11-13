from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
kafkaParams = {"metadata.broker.list": "localhost:9092"}

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext(appName="NetworkWordCount")
ssc = StreamingContext(sc, 1)
kvs = KafkaUtils.createDirectStream(ssc,["test"],kafkaParams=kafkaParams)
model = RandomForestModel.load(sc,"ForestModel")

def sendRecord(record):
    values = record.collect()
    for i in values:
        data = i[1]
        finaldata = data.split(" ")
        prediction = model.predict(finaldata)
        print(prediction)

    # prediction = model.predict(record)
    # values = prediction.collect()
    # print(values)
    print("Its RDD")
    

kvs.foreachRDD(sendRecord)
print("Stream Running ")

ssc.start()
ssc.awaitTermination()


# from pyspark import SparkContext
# # $example on$
# from pyspark.mllib.tree import RandomForest, RandomForestModel
# sc = SparkContext(appName="PythonRandomForestRegressionExample")
# model = RandomForestModel.load(sc,"target/tmp/myRandomForestRegressionModel")

# result = model.predict(data)
# print(result)
