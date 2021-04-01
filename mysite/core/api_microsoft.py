from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import requests
import os, requests, uuid, json

URL = "" # Yandex API URL
KEY = "" # Yandex API ключ
# Azure Computer Vision
endpoint = ''
subscription_key = ''


def translate_me(mytext):

    params = {
        "key": KEY,
        "text": mytext,
        "lang": 'en-ru' #Здесь мы указываем с какого языка на какой мы делаем переводим
    }
    response = requests.get(URL ,params=params)
    return ((response.json()))

def api(name):
'
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    local_image_description = computervision_client.describe_image_in_stream(name)
    x = []
    if (len(local_image_description.captions) == 0):
        x.append("No captions detected.")
    else:
        for caption in local_image_description.captions:
            x.append((translate_me(("{}".format(caption.text)))['text']))
        return x[0]


