from __future__ import print_function

# $example on$
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
# $example off$
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("NaiveBayesExample")\
        .getOrCreate()

    # $example on$
    # Load training data
    data = spark.read.format("libsvm") \
        .load("predia1.txt")

    # Split the data into train and test
    splits = data.randomSplit([0.6, 0.4], 1234)
    train = splits[0]
    test = splits[1]

    # create the trainer and set its parameters
    nb = NaiveBayes(smoothing=1.0, modelType="multinomial")

    # train the model
    model = nb.fit(train)
    f = open("Results1.txt","w")



    # select example rows to display.
    predictions = model.transform(test)

    final_data = predictions.collect()
    for i in final_data:
        f.write(str(i) + "\n")

    # compute accuracy on the test set
    evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction",
                                                  metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Test set accuracy = " + str(accuracy))
    f.close()
    model.save("FindProbability")

    spark.stop()