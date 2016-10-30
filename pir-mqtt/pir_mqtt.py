from gpiozero import MotionSensor
import paho.mqtt.publish as publish
import os

# publish a message then disconnect.
host = os.environ['MQTT_HOST']
topic = os.environ['MQTT_TOPIC']
pin = int(os.environ['PIN_INPUT'])

#pir sensor
pir = MotionSensor(pin)
curren_status = 0
last_status = 0

while True:
    curren_status = pir.motion_detected

    if curren_status and curren_status!=last_status:
        print("Motion detected!")
        publish.single(topic, 1, qos=1, hostname=host)
    elif not curren_status and curren_status!=last_status:
        print("Nothing")
        publish.single(topic, 0, qos=1, hostname=host)
    last_status = curren_status
