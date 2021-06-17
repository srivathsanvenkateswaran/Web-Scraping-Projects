# File to contain all the code to scrape the contents from https://www.discudemy.com  

# First, we will scraper discudemy.com
import os
from sys import dont_write_bytecode
from bs4 import BeautifulSoup
import requests

def getCourseLink(courseArticleLink):
    courseArticleHTML = requests.get(courseArticleLink).text
    # We get the course article html from the course article link 
    s = BeautifulSoup(courseArticleHTML, 'lxml')
    # We create a BeautifulSoup instance with the course article HTML
    takeCourseLink = s.find('a', class_ = 'ui big inverted green button discBtn')['href']
    # We find the take course link by parsing the course article 
    takeCoursePageHTML = requests.get(takeCourseLink).text
    # Now we navigate to the take course page and then we get the html of it by performing a get request with the take course link 
    s = BeautifulSoup(takeCoursePageHTML, 'lxml')
    # We parse the takeCoursePageHTML
    return s.find('div', class_ = 'ui segment').a['href']
    # Here we return the link of the original udemy course 



courseCategory = input('Enter the course category: ')
# Get the category from the User

URL = f'https://www.discudemy.com/category/{courseCategory}'
# This is the discudemy URL

print(f'Fetching courses on {courseCategory}...... ')

pageHTML = requests.get(URL).text
# This returns a response object and we extract the text[HTML] from it
soup = BeautifulSoup(pageHTML, 'lxml')
# Here we are creating a BeautifulSoup instance.

# First we will work with a single card and then will extend the logic to work with all the cards.
courseCards = soup.find_all('section', class_ = 'card')

# We find the card which contains all the course information

print(f'Parsing courses on {courseCategory}...... ')
# Parsing the cards.
for index,courseCard in enumerate(courseCards):
    courseLanguage = courseCard.find('label', class_ = 'ui green disc-fee label').text.strip()
    # Now we are getting the course language [Since we need to filter the courses based upon the Language too]

    if 'Ads' not in courseLanguage:
        # We check whether it is a course or is an Ad as we don't need to waste resources parsing ad [It might even raise exceptions as some of the elements might not be present]
        courseTitle = courseCard.find('div', class_ = 'content').find('div', class_ = 'header').a.text.strip()
        # We parse through the html to get the course Title
        courseArticleLink = courseCard.find('div', class_ = 'content').find('div', class_ = 'header').a['href']
        # We parse through the html to get the article Link
        courseDescription = courseCard.find('div', class_ = 'content').find('div', class_ = 'description').text.strip()
        # Next we parse through the html to get the description about the course 
        courseDate = courseCard.find('div', class_ = 'content').find('div', class_ = 'meta').find('span', class_ = 'category').div.text.strip()
        # Here we parse through the html to get the course date 
        courseLink = getCourseLink(courseArticleLink)
        # We get the courseLink with the help of courseArticleLink using the getCourseLink function

        if not (os.path.isdir(f'{courseCategory.strip().lower()}')):
            print(f'Creating {courseCategory.strip().lower()} directory......')
            os.mkdir(f'{courseCategory.strip().lower()}')
        # We create the directory in the name of the courseCategory if the directory doesn't exist

        with open(f'{courseCategory.strip().lower()}/{courseCategory.strip().lower()}CourseNumber{index+1}.txt', 'w') as f:
            # I have chosen the course category [in lowercase to avoid duplicates between android and Android] along with the course Number as the file name 
            f.write(f'\n---------- Course Number: {index+1} ----------\n')
            f.write(f'courseTitle: {courseTitle}\n')
            f.write(f'courseLanguage: {courseLanguage}\n')
            f.write(f'courseDescription: {courseDescription}\n')
            f.write(f'courseArticleLink: {courseArticleLink}\n')
            f.write(f'courseLink: {courseLink}\n')
            f.write(f'courseDate: {courseDate}\n')
            f.write('\n')
            # We need the \n character in each string inside f.write because that will help us in providing the file a better readability

        print(f'File android/{courseCategory.strip().lower()}CourseNumber{index+1}.txt saved successfully')


# THINGS TO BE DONE   

# parse courseImageLink
# Plan JSON Structure after scraping other similar websites. 