import os, sys, time
from datetime import datetime

def get_work_file(filename):
    return os.path.join('.', 'xml', '{0}.xml'.format(filename))
    
def write_date(file_path, interval):
    while True:
        work_file = open(file_path, 'w')
        work_file.write(str(datetime.now()))
        work_file.close()
        time.sleep(interval)