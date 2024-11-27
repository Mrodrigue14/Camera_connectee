from image_analyzer import ImageAnalyzer
from send_sms import sends_sms
from picamzero import Camera
from time import sleep

class SignalMqtt:

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
        ENDPOINT = "https://ressourcevisionus3.cognitiveservices.azure.com/"
        KEY      = "BdarwcuLHS51halnVv90SvqG5XRQwpaH5LC1SOwqX5yKH8hgUC7FJQQJ99AKACYeBjFXJ3w3AAAFACOGOxti"
        msg.payload = msg.payload.decode("utf-8")
        if msg.payload == "Motion detected":
            cam = Camera()
            cam.take_photo("photo.jpg")
            with open("photo.jpg", "rb") as f:
                image_data = f.read()
            analyzer = ImageAnalyzer(endpoint=ENDPOINT, key=KEY)
            human_detected = analyzer.analyze_image(image_data)
            if human_detected:
                print("Un humain a été détecté dans l'image.")
                sends_sms("human")
            else:
                print("Aucun humain détecté dans l'image.")
        print(msg.topic+" "+str(msg.payload))

    def on_connect(self,client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
        else:
            client.subscribe("paho/MotionDetector/motion",qos=1)