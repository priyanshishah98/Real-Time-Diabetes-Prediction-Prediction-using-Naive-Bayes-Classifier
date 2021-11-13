from flask import Flask, abort, request 
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark import SparkContext
import json
sc = SparkContext(appName="FlaskSparkTry")
model = RandomForestModel.load(sc,"ForestModel")


app = Flask(__name__)


@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    print(request.json)
    data = request.json
    age = data["age"]
    haemo = data["haemo"]
    BMI = data["BMI"]
    userParameters = [age,haemo,BMI]
    prediction = model.predict(userParameters)
    return json.dumps(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)