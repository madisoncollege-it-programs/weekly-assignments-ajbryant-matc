#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Import and copy website data as an html file.

import requests

response = requests.get("http://notpurple.com")

with open("my_web_file.html", 'w') as hFile:
    hFile.write(response.text)
