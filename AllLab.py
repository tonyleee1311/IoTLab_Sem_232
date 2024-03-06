import sys
from Adafruit_IO import MQTTClient
import time
import random
from simpleAI import *
AIO_AI_FEED=""
AIO_FEED_ID = ["",""]
AIO_USERNAME = ""
AIO_KEY = ""
AIO_FEED_SENSOR =["", "", ""]
ai_result=["",""]
ai_previous_result=["",""]
def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id: "+ feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter=10
sensorType=0
counterAI=10
while True:
    counter=counter-1
    counterAI= counterAI-1
    if(counter<=0):
        counter=10
        #todo
        print("Random data is publishing ...")
        if sensorType==0:
            temp= random.randint(10,50)
            print(f"Temperature: {temp}")
            client.publish(AIO_FEED_SENSOR[sensorType],temp)
            sensorType = 1
        elif sensorType==1:
            humid = random.randint(50, 70)
            print(f"Humidity: {humid}")
            client.publish(AIO_FEED_SENSOR[sensorType], humid)
            sensorType = 2
        elif sensorType==2:
            light = random.randint(100, 500)
            print(f"Light: {light}")
            client.publish(AIO_FEED_SENSOR[sensorType], light)
            sensorType = 0
    if(counterAI<=0):
        counterAI=10
        #todo
        ai_previous_result=ai_result
        ai_result= cameraDetector()
        print(f'AI result: {ai_result[0]}, with confidence score: {ai_result[1]}')
        if (ai_previous_result[0] != ai_result[0]):
            finalResult= ai_result[0] + " \nWith confidence score " + ai_result[1]
            #print(finalResult)
            client.publish(AIO_AI_FEED,finalResult)
    time.sleep(1)
    pass