from bs4 import BeautifulSoup
import requests
import json

topicDict = dict()

URL = 'https://www.geeksforgeeks.org/c-plus-plus/'

HTML = requests.get(URL).text

soup = BeautifulSoup(HTML, 'lxml')

def classParserOl(className):
    classOL = soup.find('div', class_ = f"{className}").ol

    d = dict()
    
    for li in classOL.find_all("li"):
        articleName = li.text
        articleLink = li.a['href']

        d[f'{articleName}'] = articleLink
        
    return d

def parseSTL():
    tags = soup.find('div', class_ = 'STL').find_all('a')
    d = dict()
    
    for tag in tags:
        if 'Practice' in tag.text:
            continue

        text = tag.text
        link = tag['href']
        d[f'{text}'] = link
    
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
    topicDict['Basics'] = classParserOl('Basics')
    topicDict['C vs C++'] = classParserOl('C vs C++')
    topicDict['C++vsJava'] = classParserOl('C++vsJava')
    topicDict['Input and Output'] = classParserOl('Input and Output')
    topicDict['Operators'] = classParserOl('Operators')
    topicDict['Arrays and Strings'] = classParserOl('Arrays and Strings')
    topicDict['Functions'] = classParserOl('Functions')
    topicDict['References and Pointers'] = classParserOl('References and Pointers')
    topicDict['Dynamic memory allocation'] = classParserOl('Dynamic memory allocation')
    topicDict['Object Oriented Programming'] = classParserOl('oop')
    topicDict['Constructor and Destructor'] = classParserOl('ConstructorandDestructor')
    topicDict['Function Overloading'] = classParserOl('FunctionOverloading')
    topicDict['Operator Overloading'] = classParserOl('OperatorOverloading')
    topicDict['Virtual Functions'] = classParserOl('VirtualFunctions')
    topicDict['Exception Handling'] = classParserOl('ExceptionHandling')
    topicDict['Namespace'] = classParserOl('Namespace')
    topicDict['STL'] = parseSTL()
    topicDict['Inheritance'] = classParserUl('Inheritance')
    topicDict['C++Library'] = classParserOl('C++Library')
    topicDict['C++Advanced'] = classParserOl('C++Advanced')
    topicDict['C++inCompetitiveProgramming'] = classParserOl('C++inCompetitiveProgramming')
    topicDict['Puzzles'] = classParserOl('Puzzles')
    topicDict['InterviewQuestions'] = classParserOl('InterviewQuestions')

    return topicDict     

if __name__ == '__main__':
    topicJson = json.dumps(constructDict(), indent=4)
    with open('GFG Cpp.json', 'w') as f:
        f.write(topicJson)

# Basics 
# C vs C++
# C++vsJava
# Input and Output
# Operators
# Arrays and Strings
# Functions
# Pointers and References
# Dynamic Memory Allocation
# Object Oriented Programming
# Constructor and Destructor
# Function Overloading
# Operator Overloading
# Virtual Functions
# Exception Handling
# Namespace
# STL 
#     Algorithms
#     Containers
#     Multimap
#     CPP-Math
#     More:
# Inheritance
# C++Library
# C++Advanced
# C++inCompetitiveProgramming
# Puzzles
# InterviewQuestions

