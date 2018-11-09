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
import pickle
from datetime import datetime

CONFIG_FILE = 'sat_settings.json'

class MySensor(Sensor):

    def __init__(self):
        """ read sensor settings from config file """
        with open(CONFIG_FILE) as json_text:
            self.__settings = json.load(json_text)
        self.__url = self.__settings.get('service_url')
        self.sat_responses = {}
        print("This sensor just woke up .. ready to call " + self.__url)

    def get_data(self):
        r = requests.get(self.__url + '32.910/-117.110/0/70/15/&apiKey=GY8YQR-CS22QC-ZLP9Y4-3WPU')
        if r.status_code == 200:
            result = r.json



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