import os
import random
import requests
from bs4 import BeautifulSoup as bs
from lxml import html
from openpyxl import Workbook


def get_random_courses_list(url):
    courses_quantity = 20
    context = requests.get(url)
    courses_tree = html.fromstring(context.content)
    courses_list = courses_tree.xpath('//loc/text()')
    random_courses_list = random.sample(courses_list, courses_quantity)
    return random_courses_list


def get_courses_info_list(random_courses_list):
    courses_info_list = []
    for course in random_courses_list:
        doc = requests.get(course)
        doc.encoding = 'UTF-8'
        parse_info = bs(''.join(doc.text), "lxml")
        course_name = parse_info.find('h1', {'class': 'title display-3-text'})
        start_date = parse_info.find(
            'div', {'class': 'startdate rc-StartDateString caption-text'}
            )
        language = parse_info.find('div', {'class': 'rc-Language'})
        rate = parse_info.find('div', {'class': 'ratings-text bt3-visible-xs'})
        course_duration = len(parse_info.findAll('div', {'class': 'week'}))
        course_info = {
            'course_name': course_name.text,
            'starting_date': start_date.text,
            'course_lang': language.text,
            'course_rate': rate.text
            if rate is not None
            else 'Not rated yet',
            'course_duration': course_duration
        }
        courses_info_list.append(course_info)
    return courses_info_list


def output_courses_info_to_xlsx(courses_info_list):
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Course name'
    ws['B1'] = 'Course language'
    ws['C1'] = 'Start course date'
    ws['D1'] = 'Course duration(on weeks)'
    ws['E1'] = 'Course rate'
    for course in courses_info_list:
        ws.append([course['course_name'],
                   course['course_lang'],
                   course['starting_date'],
                   course['course_duration'],
                   course['course_rate']
                   ])
    wb.save('Coursera.xlsx')


if __name__ == '__main__':
    url = 'http://www.coursera.org/sitemap~www~courses.xml'
    try:
        print('Please wait.')
        random_courses_list = get_random_courses_list(url)
        courses_info_list = get_courses_info_list(random_courses_list)
    except ValueError:
        print('Error! Please check xml URL')
    except requests.exceptions.ConnectionError:
        print('Error!Please check your connection')
    else:
        output_courses_info_to_xlsx(courses_info_list)
        print('Coursera.xlsx was created in folder', os.getcwd())
