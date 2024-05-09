import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))
    client.subscribe("chuobr")

#def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))
increment = 0
def publish_incrementing_value(increment):
    while True:
        increment = increment + 1
        print(increment)
        return increment


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
#mqttc.on_message = on_message

mqttc.connect("test.mosquitto.org", 1883, 60)


while True:
    mqttc.publish('chuobr', publish_incrementing_value(increment))
    time.sleep(1)
    mqttc.loop()

mqttc.loop_forever()