import os, sys, time, random
from datetime import datetime
from xml.etree.ElementTree import ElementTree


def get_work_file(filename):
    return os.path.join('.', 'xml', '{0}.xml'.format(filename))


def write_date(file_path):
    curr_time = datetime.now()
    tree = ElementTree(file=file_path)

    for item in tree.getroot().iter('item'):
        if item.attrib['name'] == 'year':
            item.text = str(curr_time.year)
        elif item.attrib['name'] == 'month':
            item.text = str(curr_time.month)
        elif item.attrib['name'] == 'day':
            item.text = str(curr_time.day)
        elif item.attrib['name'] == 'daytime':
            item.text = '{0}:{1}:{2}'.format(
                curr_time.hour, curr_time.minute, curr_time.second)

    tree.write(file_path)

def write_random(file_path, min, max):
    tree = ElementTree(file=file_path)
    
    for item in tree.getroot().iter('random'):
        item.text = str(random.randrange(min, max))

    tree.write(file_path)
