#!/usr/bin/env python3

#Author: Ashley Bryant
#Description: Extract the title and link titles from an html file.

import requests
import bs4

hFile = open('my_web_file.html')
notpurpleSoup = bs4.BeautifulSoup(hFile.read(),features='html.parser')

print(notpurpleSoup.title.text)

for link in notpurpleSoup.find_all("a"):
    print(link.get_text())
