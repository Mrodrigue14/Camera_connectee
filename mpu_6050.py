import mpu6050
from time import sleep
from send_sms import sends_sms
import pygame

mpu6050 = mpu6050.mpu6050(0x68)

pygame.mixer.init()

pygame.mixer.music.load("/home/techinfo/Téléchargements/ben_no.mp3")

def read_gyroscope_data():
    gyroscope_data = mpu6050.get_gyro_data()
    return gyroscope_data

MOVEMENT_THRESHOLD = 100

def check_for_sabotage():
    gyroscope_data = read_gyroscope_data()
    if abs(gyroscope_data['x']) > MOVEMENT_THRESHOLD or abs(gyroscope_data['y']) > MOVEMENT_THRESHOLD or abs(gyroscope_data['z']) > MOVEMENT_THRESHOLD:
        print("Mouvement abrupt détecté. Envoie d'un message de sabotage.")
        sends_sms("sabotage")

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        sleep(10)

