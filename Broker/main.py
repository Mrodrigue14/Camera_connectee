import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")

def on_unsubscribe(client, userdata, mid, reason_code_list, properties):
    # Be careful, the reason_code_list is only present in MQTTv5.
    # In MQTTv3 it will always be empty
    if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
        print("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
    else:
        print(f"Broker replied with failure: {reason_code_list[0]}")
    client.disconnect()

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    if msg.payload == "Motion detected":
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
    print(msg.topic+" "+str(msg.payload))

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        client.subscribe("paho/MotionDetector/motion",qos=1)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"idSession",False)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe


mqttc.connect("10.4.1.199",1883,0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
mqttc.loop_forever()
GPIO.cleanup()
print(f"Received the following message: {mqttc.user_data_get()}")