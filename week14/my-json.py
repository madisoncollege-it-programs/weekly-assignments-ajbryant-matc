#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Translate JSON to a Python dictionary. 

import requests
import json

response = requests.get("http://ipinfo.io/8.8.8.8/json")

myDict = json.loads(response.text)

for key in myDict:
    print(f'{key} : {myDict[key]}')
