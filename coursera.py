import requests
from bs4 import BeautifulSoup as bs
from lxml import html
import random


def get_random_courses_list(url):
    courses_quantity = 20
    context = requests.get(url)
    courses_tree = html.fromstring(context.content)
    courses_list = courses_tree.xpath('//loc/text()')
    random_courses_list = random.sample(courses_list, courses_quantity)
    return random_courses_list


def get_course_info(random_courses_list):
    #course_list=[]
    for course in random_courses_list:
        doc=requests.get(course)
        course_name=html.fromstring(doc.content)
        course_info=''.join(course_name.xpath('//p[@class="body-1-text course-description"]/text()'))

"""        
        course_info=[]
        doc = requests.get(course)
        soup = bs(''.join(doc.text), "html.parser")
        course_name = soup.find('h1', {'class': 'title display-3-text'})
        print(course_name.text)
        #course_info.append({'course_name':course_name.text})
        about = soup.find('p', {'class': 'body-1-text course-description'})
        print(about.text)
        #course_info.append({'about_course': about})
        starting_date = soup.find('div', {'class': 'startdate rc-StartDateString caption-text'})
        print(starting_date.text)
        #course_info.append({'strarting_date':starting_date.text})
        language = soup.find('div', {'class': 'rc-Language'})
        print(language.text)
        #course_info.append({'language':language.text})
        rate = soup.find('div', {'class': 'ratings-text bt3-visible-xs'})
        if rate:
            #course_info.append({'rate':rate.text})
            print(rate.text)
        #course_info.append({'course_duration':len(soup.findAll('div', {'class': 'week'}))})
        #course_list.append(course_info)
    #print(len(course_list))
"""

def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    url = 'http://www.coursera.org/sitemap~www~courses.xml'
    random_courses_list = get_random_courses_list(url)
    get_course_info(random_courses_list)
