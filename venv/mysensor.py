""" 
Robert Schult
CSIS 250
Project 2
Software Sensor Application
"""

from sensor import Sensor
import json
import time
import requests
from datetime import datetime

CONFIG_FILE = 'mysensor.json'


class MySensor(Sensor):

    def __init__(self):
        """ read sensor settings from config file """
        with open(CONFIG_FILE) as json_text:
            self.__settings = json.load(json_text)
        self.__url = self.__settings.get('service_url')
        print("This sensor just woke up .. ready to call " + self.__url)

    def get_data(self):
        # https://www.n2yo.com/rest/v1/satellite/above/32.910/-117.110/0/70/15/&apiKey=GY8YQR-CS22QC-ZLP9Y4-3WPU
        pass

    def has_updates(self, k):
        pass

    def get_content(self, k):
        pass

    def get_all(self):
        pass


if __name__ == "__main__":
    sr = MySensor()
    print("This is me : " + str(sr))
    print("let's go ..")