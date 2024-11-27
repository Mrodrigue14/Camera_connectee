from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

class ImageAnalyzer:
    def __init__(self, endpoint, key):
        self.client = ImageAnalysisClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key),
            logging_enable=True
        )
    
    def analyze_image(self, image_data):
        """
        Analyse une image pour détecter la présence d'humains.

        :param image_data: Les données de l'image sous forme de bytes.
        :return: Un booléen indiquant si un humain a été détecté avec une confiance >= 0.60.
        """
        result = self.client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.PEOPLE,
            ],
            model_version="latest",
        )

        if result.people is not None and len(result.people.list) > 0:
            for person in result.people.list:
                if person.confidence >= 0.80:
                    return True  # Humain détecté avec une confiance suffisante
        return False  # Aucun humain détecté avec une confiance suffisante
