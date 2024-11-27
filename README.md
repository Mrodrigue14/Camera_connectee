# MQTT-Based Motion Detection and Sabotage Monitoring System

Ce programme intègre un capteur de mouvement, une caméra et un gyroscope avec un broker MQTT pour détecter les mouvements, analyser les images pour la présence humaine et surveiller les sabotages. Les notifications sont envoyées par SMS grâce à Twilio. Ce système est conçu pour les environnements nécessitant une surveillance en temps réel.

---

## Fonctionnalités
1. **Détection de Mouvement** : 
   - Détecte les mouvements via une caméra et publie un message MQTT.
   - Capture une image en cas de mouvement détecté et l'analyse pour détecter la présence humaine via Azure Cognitive Services.

2. **Détection de Sabotage** : 
   - Utilise un gyroscope (MPU6050) pour surveiller les mouvements brusques qui indiqueraient des tentatives de sabotage.
   - Envoie une alerte SMS en cas de sabotage détecté.

3. **Alertes en Temps Réel** :
   - Envoie des notifications par SMS pour les humains détectés ou les événements de sabotage via Twilio.

4. **Intégration MQTT** :
   - S'abonne à un sujet spécifique pour traiter les événements de mouvement et exécuter les actions correspondantes.

---

## Prérequis
- **Matériel** :
  - Capteur de mouvement (caméra).
  - Gyroscope (MPU6050).
  - Appareil avec support GPIO (par exemple, Raspberry Pi).
- **Logiciel** :
  - Broker MQTT (par exemple, Mosquitto) fonctionnant à `10.4.1.203`.
  - Azure Cognitive Services pour l'analyse des images.
  - Twilio pour les notifications SMS.

---

## Installation

1. **Installer les Dépendances** :

    Assurez-vous que Python 3.x est installé. Ensuite, installez les paquets nécessaires :
    ```bash
    pip install -r requirement.txt

2. **Configurer les Variables d'Environnement** : 
    Configurez Twilio en définissant les variables d'environnement suivantes :

    - export TWILIO_AUTH_TOKEN="votre_auth_token_twilio"
    - export TWILIO_ACCOUNT_SID="votre_account_sid_twilio"
    - Configurer Azure Cognitive Services : Mettez à jour les variables ENDPOINT et KEY dans signal_mqtt.py avec vos identifiants Azure Cognitive Services.

## Utilisation

    Démarrer le Broker MQTT :
        - Assurez-vous que le broker MQTT fonctionne sur 10.4.1.203 (ou mettez à jour l'IP dans main.py).

    Exécuter le Programme :

    python main.py

    Tester la Détection de Mouvement :
        - Provoquez un mouvement devant la caméra pour détecter et analyser la présence humaine.
        - Des alertes SMS seront envoyées si une présence humaine est détectée.

    Tester la Détection de Sabotage :
        - Simulez des mouvements brusques sur le gyroscope. Une alerte SMS sera envoyée en cas de sabotage détecté.

## Description des Fichiers
main.py

    - Initialise le client MQTT et configure les callbacks pour la détection de mouvement et de sabotage.

signal_mqtt.py

    - Contient la classe SignalMqtt avec les méthodes pour gérer les événements MQTT et l'analyse d'images.

mpu_6050.py

    - Surveille les données du gyroscope pour détecter les mouvements brusques indicatifs de sabotage.

image_analyzer.py

    - Utilise Azure Cognitive Services pour analyser les images et détecter la présence humaine.

send_sms.py

    - Envoie des notifications SMS grâce à l'API Twilio.

requirements.txt

    - Liste toutes les dépendances Python.

# Configuration de l'Environnement

    - Assurez-vous que le broker MQTT est accessible sur l'IP et le port configurés.
    - Connectez et configurez le matériel (capteur de mouvement, gyroscope) sur l'appareil.

# Notes

    - Remplacez les variables codées en dur (par exemple, IP du broker MQTT, numéro d'envoi Twilio) par les valeurs appropriées.
    - Assurez-vous que les identifiantsTwilio sont sécurisés à l'aide de variables d'environnement ou d'un coffre sécurisé.