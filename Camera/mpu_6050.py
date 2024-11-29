import mpu6050
from time import sleep
from send_sms import sends_sms
import pygame

mpu6050_sensor = mpu6050.mpu6050(0x68)

pygame.mixer.init()
pygame.mixer.music.load("/home/techinfo/Téléchargements/ben_no.mp3")

def read_gyroscope_data():
    global mpu6050_sensor
    try:
        return mpu6050_sensor.get_gyro_data()
    except Exception as e:
        print(f"Erreur lors de la lecture des données du gyroscope : {e}")
        return {"x": 0, "y": 0, "z": 0}

MOVEMENT_THRESHOLD = 100

def check_for_sabotage():
    global mpu6050_sensor
    try:
        gyroscope_data = read_gyroscope_data()

        # Vérifier si le capteur est déconnecté
        if abs(gyroscope_data['x']) == 0 and abs(gyroscope_data['y']) == 0 and abs(gyroscope_data['z']) == 0:
            print("Perte de connexion au capteur. Réinitialisation...")
            mpu6050_sensor = mpu6050.mpu6050(0x68)
            sleep(1)  # Laisser le temps au capteur de se réinitialiser

        if abs(gyroscope_data['x']) > MOVEMENT_THRESHOLD or abs(gyroscope_data['y']) > MOVEMENT_THRESHOLD or abs(gyroscope_data['z']) > MOVEMENT_THRESHOLD:
            print("Mouvement abrupt détecté. Envoie d'un message de sabotage.")
            sends_sms("sabotage")

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            sleep(10)
    except Exception as e:
        print(f"Erreur détectée lors de la vérification du sabotage : {e}")
