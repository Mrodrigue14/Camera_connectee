import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from gpiozero import LED, MotionSensor
import signal
import sys


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


led = LED(23)
pir = MotionSensor(4)


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("10.4.1.203", 1883, 60)
mqttc.loop_start()


def cleanup(signal, frame):
    led.off()
    print("Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)

try:
    while True:
        pir.wait_for_motion()
        print("Motion detected")
        led.on()


        mqttc.publish("paho/MotionDetector/motion", "Motion detected", qos=0, retain=True)

        time.sleep(2)
        

        pir.wait_for_no_motion()
        led.off()
        print("No motion detected")
        

        mqttc.publish("paho/MotionDetector/motion", "No motion detected", qos=0, retain=True)

except Exception as e:
    print(f"An error occurred: {e}")
    cleanup(None, None)