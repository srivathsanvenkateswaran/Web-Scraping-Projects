from bs4 import BeautifulSoup
import requests
import json

topicDict = dict()

URL = 'https://www.geeksforgeeks.org/operating-systems/'

HTML = requests.get(URL).text

soup = BeautifulSoup(HTML, 'lxml')

def classParser(className):
    classOL = soup.find('div', class_ = f"{className}").ol

    d = dict()
    
    for li in classOL.find_all("li"):
        articleName = li.text
        articleLink = li.a['href']

        d[f'{articleName}'] = articleLink
        
    return d

def classParserUl(className):
    classUl = soup.find('div', class_ = f"{className}").ul

    d = dict()
    
    for li in classUl.find_all("li"):
        articleName = li.text
        articleLink = li.a['href']

        d[f'{articleName}'] = articleLink
        
    return d

def constructDict():
    topicDict['Basics'] = classParser('basics')
    topicDict['System Structure'] = classParser('sys')
    topicDict['CPU Scheduling'] = classParser('cpu')
    topicDict['Process Synchronization'] = classParser('syn')
    topicDict['Deadlock'] = classParser('deadlock')
    topicDict['Processes & Thread'] = classParser('threads')
    topicDict['Memory Management'] = classParser('mmgmt')
    topicDict['Disk Management'] = classParser('disk')
    topicDict['Misc'] = classParser('misc')
    topicDict['Quick Links'] = classParserUl('misc')
    return topicDict

if __name__ == '__main__':
    topicJson = json.dumps(constructDict(), indent=4)
    with open('GFG OS.json', 'w') as f:
        f.write(topicJson)