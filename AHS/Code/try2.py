from kafka import KafkaConsumer
from json import loads
import pandas as pd 

main_values = []

consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

# for message in consumer:
#     message = message.value
#     print(message)

for message in consumer:
    message = message.value
    values = []
    values.append(message["a1"])
    values.append(message["a2"])
    values.append(message["a3"])
    values.append(message["a4"])    
    values.append(message["a5"])
    print(values)
    main_values.append(values)
    main_df = pd.DataFrame(main_values)
    main_df.to_csv("kafkapython.csv",mode="a")
