import random
import requests
from bs4 import BeautifulSoup as bs
from lxml import html
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment


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
        course_content = html.fromstring(doc.content)
        course_name = '//h1[@class="title display-3-text"]/text()'
        start_date = '//div[@class="startdate rc-StartDateString caption-text"]/span/text()'
        course_lang = '//div[@class="rc-Language"]/text()'
        course_rate = '//div[@class="ratings-text bt3-visible-xs"]/text()'
        course_duration = 'count(//*[@class="week"])'
        course_info = {
            'course_name': ''.join(course_content.xpath(course_name)),
            'starting_date': ''.join(course_content.xpath(start_date)),
            'course_lang': ''.join(course_content.xpath(course_lang)),
            'course_rate': ''.join(course_content.xpath(course_rate)),
            'course_duration': course_content.xpath(course_duration)
        }
        courses_info_list.append(course_info)
    return courses_info_list


def output_courses_info_to_xlsx(courses_info_list):
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Course name'
    ws['B1'] = 'Course language'
    ws['C1'] = 'Start course date'
    ws['D1'] = 'Course duration(weeks)'
    ws['E1'] = 'Course rate'
    for course in courses_info_list:
        ws.append([course['course_name'],
                   course['course_lang'],
                   course['starting_date'],
                   course['course_duration'],
                   course['course_rate']
                   if course['course_rate'] != ''
                   else 'Not rated yet',
                   ])
    wb.save('Coursera.xlsx')


if __name__ == '__main__':
    url = 'http://www.coursera.org/sitemap~www~courses.xml'
    random_courses_list = get_random_courses_list(url)
    courses_info_list = get_courses_info_list(random_courses_list)
    output_courses_info_to_xlsx(courses_info_list)
