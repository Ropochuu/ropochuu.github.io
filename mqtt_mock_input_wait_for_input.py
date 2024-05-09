import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code "+str(reason_code))
    client.subscribe("chuobr")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def wait_for_user_input(msg):
    message = msg
    return message
# TO DO - Create a function to prompt the user for an int with error handling 

       

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("test.mosquitto.org", 1883, 60)



# Wait for user input
user_input = wait_for_user_input()

# If user input is valid, publish it to the MQTT topic
if user_input is not None:
    mqttc.publish("chuobr", user_input)
    print("Published: " + user_input)
  

mqttc.loop_forever()
