import re
from urllib import request
from lxml import etree


def get_courses_list(url):
    context = etree.iterparse(url)
    url_list_of_courses = []
    for action, course_url in context:
        if re.findall(r'\w', course_url.text):
            url_list_of_courses.append(course_url.text)
    print(url_list_of_courses)


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    url=request.urlopen('http://www.coursera.org/sitemap~www~courses.xml')
    get_courses_list(url)