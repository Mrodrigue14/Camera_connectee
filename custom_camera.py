from picamzero import Camera
from image_analyzer import ImageAnalyzer
from send_sms import sends_sms
class CustomCamera:
    ENDPOINT = "https://ressourcevisionus3.cognitiveservices.azure.com/"
    KEY      = "BdarwcuLHS51halnVv90SvqG5XRQwpaH5LC1SOwqX5yKH8hgUC7FJQQJ99AKACYeBjFXJ3w3AAAFACOGOxti"
    def on_motion_detected(self):

        cam = Camera()
        cam.take_photo("photos/photo.jpg")
        with open("photos/photo.jpg", "rb") as f:
            image_data = f.read()
        analyzer = ImageAnalyzer(endpoint=self.ENDPOINT, key=self.KEY)
        human_detected = analyzer.analyze_image(image_data)
        if human_detected:
            print("Un humain a été détecté dans l'image.")
            sends_sms("human")
        else:
            print("Aucun humain détecté dans l'image.")