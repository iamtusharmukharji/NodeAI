import paho.mqtt.client as mqtt
from app.cred_loder import creds
import json


MQTT_HOST = creds.mqtt["MQTT_HOST"]
PORT = creds.mqtt["MQTT_PORT"] 
DATA_TOPIC = creds.mqtt["DATA_TOPIC"]


class NodeMQTT:

    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.device_data = None

    def on_connect_callback(self, *args):
        self.mqtt_client.subscribe(topic = DATA_TOPIC, qos = 0)
        print("Connected to MQTT Broker")
        
    def on_recv_msg_callback(self, client, userdata, message):
        self.device_data = json.loads(message.payload.decode())

    def connect_mqtt(self):
        self.mqtt_client.on_connect = self.on_connect_callback
        self.mqtt_client.on_message = self.on_recv_msg_callback

        self.mqtt_client.connect_async(MQTT_HOST, PORT, 60)
        self.mqtt_client.loop_start()

    def publish_mqtt(self, topic: str, payload: dict):
        self.mqtt_client.publish(topic, json.dumps(payload), qos=1)


node_mqtt = NodeMQTT()