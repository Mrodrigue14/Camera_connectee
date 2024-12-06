from image_analyzer import ImageAnalyzer
from picamzero import Camera
from time import sleep

class SignalMqtt:

    def __init__(self):
        self.callbacks =  []
    def subscribes(self, callback):
        self.callbacks.append(callback)

    def notify(self):
        for fn in self.callbacks:
            fn()


    def on_subscribe(self,client, userdata, mid, reason_code_list, properties):
        if reason_code_list[0].is_failure:
            print(f"Broker rejected you subscription: {reason_code_list[0]}")
        else:
            print(f"Broker granted the following QoS: {reason_code_list[0].value}")

    def on_unsubscribe(self,client, userdata, mid, reason_code_list, properties):
        if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
            print("unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)")
        else:
            print(f"Broker replied with failure: {reason_code_list[0]}")
        client.disconnect()

    def on_message(self,client, userdata, msg):
        msg.payload = msg.payload.decode("utf-8")
        if msg.payload == "Motion detected":
            self.notify()
        print(msg.topic+" "+str(msg.payload))

    def on_connect(self,client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
        else:
            client.subscribe("paho/MotionDetector/motion",qos=1)