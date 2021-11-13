from __future__ import print_function

import shutil

from pyspark import SparkContext
# $example on$
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.util import MLUtils


# $example off$

if __name__ == "__main__":

    sc = SparkContext(appName="PythonNaiveBayesExample")

    # $example on$
    # Load and parse the data file.
    data = MLUtils.loadLibSVMFile(sc, "libsvmdata.txt")

    # Split data approximately into training (60%) and test (40%)
    training, test = data.randomSplit([0.6, 0.4])

    # Train a naive Bayes model.
    model = NaiveBayes.train(training, 1.0)

    # Make prediction and test accuracy.
    predictionAndLabel = test.map(lambda p: (model.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda pl: pl[0] == pl[1]).count() / test.count()
    print('model accuracy {}'.format(accuracy))

    # Save and load model
    output_dir = 'myNaiveBayesModel'
    shutil.rmtree(output_dir, ignore_errors=True)
    model.save(sc, output_dir)
    sameModel = NaiveBayesModel.load(sc, output_dir)
    predictionAndLabel = test.map(lambda p: (sameModel.predict(p.features), p.label))
    accuracy = 1.0 * predictionAndLabel.filter(lambda pl: pl[0] == pl[1]).count() / test.count()
    print('sameModel accuracy {}'.format(accuracy))