import paho.mqtt.client as mqtt
from app.cred_loder import creds
import json


MQTT_HOST = creds.mqtt["MQTT_HOST"]
PORT = creds.mqtt["MQTT_PORT"] 

mqtt_client = mqtt.Client()

def connect_mqtt():
    mqtt_client.connect(MQTT_HOST, PORT, 60)
    mqtt_client.loop_start()
    return mqtt_client

def publish_mqtt(topic: str, payload: dict):
    mqtt_client.publish(topic, json.dumps(payload), qos=1)