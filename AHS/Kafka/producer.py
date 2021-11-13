from kafka import KafkaProducer
from kafka.errors import KafkaError
import pandas as pd
import json

mainFile = pd.read_csv("classify3.csv")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])




#  'Haemoglobin', 'BP1', 'BP2', 'BP3', 'BP4', 'Pulse', 'Pulse2', 'fasting', 'BMI', 'Diabetes']

for index,row in mainFile.iterrows(): 
	weight = row["Weight"]
	height = row["Height"]
	haemoglobin = row["Haemoglobin"]
	sex = row["Sex"]

	user = {
		"Weight":weight,
		"Sex":sex,
		"Height":height,
		"Haemo":haemoglobin
	}

	user_str = json.dumps(user)
	userfinal = user_str.encode('utf8')
	index = str(index).encode('utf8')

	producer.send('test',key=b"1",value=userfinal)



# loc = [b"a",b"b",b"c"];
# for i in loc:
# 	producer.send('test',key=b"1",value=i)
	
# # produce keyed messages to enable hashed partitioning
# producer.send('test', key=b'g1g', value=b'new values incoming')

# block until all async messages are sent
producer.flush()
