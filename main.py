import paho.mqtt.client as mqtt
from mpu_6050 import check_for_sabotage  
from signal_mqtt import SignalMqtt
from speaker import ConnectBluetooth
import os

bluetooth_address = "F4:4E:FD:7A:94:BA"
volume_level = 40
bt_connection = ConnectBluetooth(bluetooth_address, volume_level)

bt_connection.connect_device()

signal_mqtt = SignalMqtt()

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"idSession",False)
mqttc.on_connect = signal_mqtt.on_connect
mqttc.on_message = signal_mqtt.on_message
mqttc.on_subscribe = signal_mqtt.on_subscribe
mqttc.on_unsubscribe = signal_mqtt.on_unsubscribe


mqttc.connect("10.4.1.203",1883,0)

while True:
    os.system(f"amixer sset 'Master' {volume_level}%  > /dev/null 2>&1")
    check_for_sabotage()
    mqttc.loop(0.1) 