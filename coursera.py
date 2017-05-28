import re
import random
import requests
from urllib import request
from lxml import etree
from bs4 import BeautifulSoup as bs


def get_courses_list(url):
    context = etree.iterparse(url)
    list_of_courses = []
    courses_quantity = 20
    for action, course_url in context:
        if re.findall(r'\w', course_url.text):
            list_of_courses.append(course_url.text)
    random_courses_list = random.sample(list_of_courses, courses_quantity)
    return random_courses_list


def get_course_info(random_courses_list): # TODO Make list of info params and for...(if..else) cycle.
    for course in random_courses_list:
        doc = requests.get(course)
        soup = bs(''.join(doc.text), "html.parser")
        Current_tag = soup.find('h1', {'class': 'title display-3-text'})  # Course name
        print(Current_tag.text)  # Course name
        Current_tag = soup.find('p', {'class': 'body-1-text course-description'})  # About course
        print(Current_tag.text)  # About course
        Current_tag = soup.find('div', {'class': 'startdate rc-StartDateString caption-text'})  # Starting date
        print(Current_tag.text)  # Starting date
        Current_tag = soup.find('div', {'class': 'rc-Language'})  # Language
        print(Current_tag.text)  # Language
        Current_tag = soup.find('div', {'class': 'ratings-text bt3-visible-xs'})  # Rate
        if Current_tag:
            print(Current_tag.text)  # Rate
        else:
            print(len(soup.findAll('div',{'class':'week'}))) # Weeks


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    url = request.urlopen('http://www.coursera.org/sitemap~www~courses.xml')
    random_courses_list=get_courses_list(url)
    get_course_info(random_courses_list)
