import cv2
import numpy as np
import time
from datetime import datetime
import requests
import pip
try:
    __import__(azure.storage.blob)
except ImportError:
    pip.main(['install', azure.storage.blob])   
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
from azure.storage.blob import ContentSettings
import json

 

vcap = cv2.VideoCapture("rtsp://nvidia:nvidia@192.168.87.184/axis-media/media.amp")

ret, frame = vcap.read()

for i in range(0, 10):
    ret, frame = vcap.read()
    if frame is not None:
        filename = f"{i}.jpg"
        cv2.imwrite(filename, frame)

        blob_client = BlobClient(account_url="https://smartofficentt.blob.core.windows.net", credential='sp=racwdl&st=2021-09-06T06:46:31Z&se=2022-04-07T14:46:31Z&sv=2020-08-04&sr=c&sig=9CfAS8%2FX%2B5T4rXQHGWGELjWvjIWU%2BM7OqN2zHRIKb9A%3D', container_name='ntt-smartoffice', blob_name=filename)

        image_content_setting = ContentSettings(content_type='image/jpeg')
        print(f"uploading file - {filename}")
        with open(f"./{filename}", "rb") as data:
            blob_client.upload_blob(data,overwrite=True,content_settings=image_content_setting)
    time.sleep(1)

vcap.release()
