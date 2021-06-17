import json
from bs4 import BeautifulSoup
import requests

from requests.api import request

HOME_URL = "https://zerodha.com/varsity/"

def parseHome(HOME_URL):
    VARSITY_HTML = requests.get(HOME_URL).text
    soup = BeautifulSoup(VARSITY_HTML, 'lxml')
    moduleUL = soup.find('ul', class_='noul row')

    d = dict()

    for li in moduleUL.find_all('li'):
        moduleName = li.h4.a.text
        moduleLink = li.h4.a['href']
        d[moduleName] = parseModules(moduleLink)

    return d

def parseModules(MODULE_URL):
    MODULE_HTML = requests.get(MODULE_URL).text
    soup = BeautifulSoup(MODULE_HTML, 'lxml')
    chapterUL = soup.find('ul', class_ = 'noul')

    d = dict()

    for li in chapterUL.find_all('li'):
        chapterName = li.h4.a.text
        chapterLink = li.h4.a['href']
        d[chapterName] = chapterLink
    
    return d
        

s = parseHome(HOME_URL)

with open('varsity.json', 'w') as f:
    json.dump(s, f, indent=4)