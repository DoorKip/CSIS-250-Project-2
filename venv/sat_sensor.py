""" 
Robert Schult
CSIS 250
Project 2
Software Sensor Application
"""

from sensor import SensorX
import json
import time
import requests
import pickle
from datetime import datetime

CONFIG_FILE = 'sat_settings.json'

class MySensor(SensorX):

    def __init__(self):
        """ read sensor settings from config file """
        with open(CONFIG_FILE) as json_text:
            self.__settings = json.load(json_text)
            self.__url = self.__settings.get('service_url')
            self.__key = self.__settings.get('api_key')
            self.__lat = self.__settings.get('location_lat')
            self.__lon = self.__settings.get('location_lon')
            self.__alt = self.__settings.get('location_alt')
            self.__arc = self.__settings.get('search_arc')
            self.__cat = self.__settings.get('sat_category')
        self.sat_responses = {}
        print("This sensor just woke up .. ready to call " + self.__url)

    def __str__(self):
        return(self.get_all())

    def get_data(self):
        # Runs the rest api request to get the current list of satleites overhead.
        r = requests.get(self.__url + self.__lat + '/' + self.__lon + '/' + self.__alt + '/'
                         + self.__arc + '/' + self.__cat + '/&apiKey=' + self.__key)
        if r.status_code == 200:
            result = r.json()
            return str(result)
        else:
            return "Resource Not Found"

    def has_updates(self, k):
        print("Waiting on pickle implementation")

    def get_content(self, k):
        print("Waiting on pickle implementation")

    def get_all(self):
        data = self.get_data()
        return data


if __name__ == "__main__":
    sr = MySensor()
    print("Sat Data : " + str(sr))